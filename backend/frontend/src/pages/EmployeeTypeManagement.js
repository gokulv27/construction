import React, { useState, useEffect, useCallback } from 'react';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { fetchEmployeeTypes, createEmployeeType, updateEmployeeType, deleteEmployeeType } from '../api/employeeTypeApi';
import { EmployeeTypeForm } from '../components/EmployeeTypeForm';
import { EmployeeTypeTable } from '../components/EmployeeTypeTable';
import '../styles/MasterPageManagement.css';
import TopNav from '../components/TopNav';

const EmployeeTypeManagement = () => {
  const [employeeTypes, setEmployeeTypes] = useState([]);
  const [filteredEmployeeTypes, setFilteredEmployeeTypes] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [currentEmployeeType, setCurrentEmployeeType] = useState(null);
  const [selectedIds, setSelectedIds] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    loadEmployeeTypes();
  }, []);

  useEffect(() => {
    const filtered = employeeTypes.filter(et => 
      et.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredEmployeeTypes(filtered);
  }, [searchTerm, employeeTypes]);

  const loadEmployeeTypes = async () => {
    try {
      const data = await fetchEmployeeTypes();
      setEmployeeTypes(data);
      setFilteredEmployeeTypes(data);
    } catch (error) {
      console.error('Error fetching employee types:', error);
      toast.error('Failed to fetch employee types');
    }
  };

  const handleSubmit = async (data) => {
    try {
      if (currentEmployeeType) {
        await updateEmployeeType({ ...data, id: currentEmployeeType.id });
        toast.success('Employee type updated successfully');
      } else {
        await createEmployeeType(data);
        toast.success('New employee type created successfully');
      }
      loadEmployeeTypes();
      setIsModalOpen(false);
      setCurrentEmployeeType(null);
    } catch (error) {
      console.error('Error submitting data:', error);
      toast.error('Failed to submit data');
    }
  };

  const handleEdit = (employeeType) => {
    setCurrentEmployeeType(employeeType);
    setIsModalOpen(true);
  };

  const handleDelete = async () => {
    if (currentEmployeeType) {
      try {
        await deleteEmployeeType(currentEmployeeType.id);
        toast.success('Employee type deleted successfully');
        loadEmployeeTypes();
        setIsDeleteModalOpen(false);
        setCurrentEmployeeType(null);
      } catch (error) {
        console.error('Error deleting employee type:', error);
        toast.error('Failed to delete employee type');
      }
    }
  };

  const handleSelectAll = (checked) => {
    if (checked) {
      setSelectedIds(filteredEmployeeTypes.map(et => et.id));
    } else {
      setSelectedIds([]);
    }
  };

  const handleSelectOne = (id, checked) => {
    if (checked) {
      setSelectedIds(prev => [...prev, id]);
    } else {
      setSelectedIds(prev => prev.filter(itemId => itemId !== id));
    }
  };

  const handleDeleteSelected = async () => {
    try {
      await Promise.all(selectedIds.map(id => deleteEmployeeType(id)));
      toast.success('Selected employee types deleted successfully');
      loadEmployeeTypes();
      setSelectedIds([]);
    } catch (error) {
      console.error('Error deleting selected employee types:', error);
      toast.error('Failed to delete selected employee types');
    }
  };

  const openNewEntryModal = useCallback(() => {
    setCurrentEmployeeType(null);
    setIsModalOpen(true);
  }, []);

  const handleSearch = useCallback((term) => {
    setSearchTerm(term);
  }, []);

  return (
    <>
      <TopNav openNewEntryModal={openNewEntryModal} onSearch={handleSearch} />
      <div className="box">
        <div className="box-body">
          <div className="header-container">
            <h1 className="header-title">Employee Type Management</h1>
            <button
              className="button"
              id="newEntryButton"
              onClick={openNewEntryModal}
            >
              <svg
                aria-hidden="true"
                focusable="false"
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M5 12h14" />
                <path d="M12 5v14" />
              </svg>
              New Entry
            </button>
          </div>

          {selectedIds.length > 0 && (
            <div className="mb-4">
              <button onClick={handleDeleteSelected} className="btn btn-danger">
                Delete Selected ({selectedIds.length})
              </button>
            </div>
          )}

          <EmployeeTypeTable
            employeeTypes={filteredEmployeeTypes}
            onEdit={handleEdit}
            onDelete={(employeeType) => {
              setCurrentEmployeeType(employeeType);
              setIsDeleteModalOpen(true);
            }}
            onSelectAll={handleSelectAll}
            onSelectOne={handleSelectOne}
            selectedIds={selectedIds}
          />

          {isModalOpen && (
            <div className="modal">
              <div className="modal-content">
                <span className="close" onClick={() => setIsModalOpen(false)}>&times;</span>
                <h2 className="modal-title">{currentEmployeeType ? 'Edit' : 'New'} Employee Type</h2>
                <EmployeeTypeForm
                  initialData={currentEmployeeType || undefined}
                  onSubmit={handleSubmit}
                />
              </div>
            </div>
          )}

          {isDeleteModalOpen && (
            <div className="modal">
              <div className="modal-content">
                <span className="close" onClick={() => setIsDeleteModalOpen(false)}>&times;</span>
                <h2 className="modal-title">Confirm Deletion</h2>
                <p>Are you sure you want to delete this employee type?</p>
                <div className="modal-actions">
                  <button
                    onClick={handleDelete}
                    className="btn btn-danger"
                  >
                    Delete
                  </button>
                  <button
                    onClick={() => setIsDeleteModalOpen(false)}
                    className="btn btn-secondary"
                  >
                    Cancel
                  </button>
                </div>
              </div>
            </div>
          )}

          <ToastContainer />
        </div>
      </div>
    </>
  );
};

export default EmployeeTypeManagement;

