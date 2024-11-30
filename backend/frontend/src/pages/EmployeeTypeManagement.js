import React, { useState, useEffect } from 'react';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { fetchEmployeeTypes, createEmployeeType, updateEmployeeType, deleteEmployeeType } from '../api/employeeTypeApi';
import { EmployeeTypeForm } from '../components/EmployeeTypeForm';
import { EmployeeTypeTable } from '../components/EmployeeTypeTable';
import '../styles/EmployeeTypeManagement.css';

export const EmployeeTypeManagement = () => {
  const [employeeTypes, setEmployeeTypes] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [currentEmployeeType, setCurrentEmployeeType] = useState(null);
  const [selectedIds, setSelectedIds] = useState([]);

  useEffect(() => {
    loadEmployeeTypes();
  }, []);

  const loadEmployeeTypes = async () => {
    try {
      const data = await fetchEmployeeTypes();
      setEmployeeTypes(data);
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
      setSelectedIds(employeeTypes.map(et => et.id));
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

  return (
    <div className="box">
      <div className="box-body">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold">Employee Type Management</h1>
          
        </div>

        {selectedIds.length > 0 && (
          <div className="mb-4">
            <button onClick={handleDeleteSelected} className="btn btn-danger">
              Delete Selected ({selectedIds.length})
            </button>
          </div>
        )}

        <EmployeeTypeTable
          employeeTypes={employeeTypes}
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
          <div className="modal" style={{ display: 'block' }}>
            <div className="modal-content">
              <span className="close" onClick={() => setIsModalOpen(false)}>&times;</span>
              <h2 className="text-xl font-bold mb-4">{currentEmployeeType ? 'Edit' : 'New'} Employee Type</h2>
              <EmployeeTypeForm
                initialData={currentEmployeeType || undefined}
                onSubmit={handleSubmit}
              />
            </div>
          </div>
        )}

        {isDeleteModalOpen && (
          <div className="modal" style={{ display: 'block' }}>
            <div className="modal-content">
              <span className="close" onClick={() => setIsDeleteModalOpen(false)}>&times;</span>
              <h2 className="text-xl font-bold mb-4">Confirm Deletion</h2>
              <p>Are you sure you want to delete this employee type?</p>
              <div className="mt-4">
                <button
                  onClick={handleDelete}
                  className="btn btn-danger mr-2"
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
  );
};

export default EmployeeTypeManagement;

