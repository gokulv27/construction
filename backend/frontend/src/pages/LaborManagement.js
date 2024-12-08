import React, { useState, useEffect, useCallback } from 'react';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { fetchLabors, createLabor, updateLabor, deleteLabor } from '../api/laborApi';
import { LaborForm } from '../components/LaborForm';
import { LaborTable } from '../components/LaborTable';
import '../styles/MasterPageManagement.css';
import TopNav from '../components/TopNav';

const LaborManagement = () => {
  const [labors, setLabors] = useState([]);
  const [filteredLabors, setFilteredLabors] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [currentLabor, setCurrentLabor] = useState(null);
  const [selectedIds, setSelectedIds] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    loadLabors();
  }, []);

  useEffect(() => {
    const filtered = labors.filter(labor => 
      labor.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      labor.phone_no.includes(searchTerm) ||
      labor.aadhar_no.includes(searchTerm)
    );
    setFilteredLabors(filtered);
  }, [searchTerm, labors]);

  const loadLabors = async () => {
    try {
      const data = await fetchLabors();
      setLabors(data);
      setFilteredLabors(data);
    } catch (error) {
      console.error('Error fetching labors:', error);
      toast.error('Failed to fetch labors');
    }
  };

  const handleSubmit = async (data) => {
    try {
      if (currentLabor) {
        await updateLabor({ ...data, id: currentLabor.id });
        toast.success('Labor updated successfully');
      } else {
        await createLabor(data);
        toast.success('New labor created successfully');
      }
      loadLabors();
      setIsModalOpen(false);
      setCurrentLabor(null);
    } catch (error) {
      console.error('Error submitting data:', error);
      toast.error('Failed to submit data');
    }
  };

  const handleEdit = (labor) => {
    setCurrentLabor(labor);
    setIsModalOpen(true);
  };

  const handleDelete = async () => {
    if (currentLabor) {
      try {
        await deleteLabor(currentLabor.id);
        toast.success('Labor deleted successfully');
        loadLabors();
        setIsDeleteModalOpen(false);
        setCurrentLabor(null);
      } catch (error) {
        console.error('Error deleting labor:', error);
        toast.error('Failed to delete labor');
      }
    }
  };

  const handleSelectAll = (checked) => {
    if (checked) {
      setSelectedIds(filteredLabors.map(labor => labor.id));
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
      await Promise.all(selectedIds.map(id => deleteLabor(id)));
      toast.success('Selected labors deleted successfully');
      loadLabors();
      setSelectedIds([]);
    } catch (error) {
      console.error('Error deleting selected labors:', error);
      toast.error('Failed to delete selected labors');
    }
  };

  const openNewEntryModal = useCallback(() => {
    setCurrentLabor(null);
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
            <h1 className="header-title">Labor Management</h1>
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

          <LaborTable
            labors={filteredLabors}
            onEdit={handleEdit}
            onDelete={(labor) => {
              setCurrentLabor(labor);
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
                <h2 className="modal-title">{currentLabor ? 'Edit' : 'New'} Labor</h2>
                <LaborForm
                  initialData={currentLabor || {}}
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
                <p>Are you sure you want to delete this labor?</p>
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

export default LaborManagement;
