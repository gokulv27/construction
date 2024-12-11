import React, { useState, useEffect, useCallback } from 'react';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { fetchLaborSkills, createLaborSkill, updateLaborSkill, deleteLaborSkill } from '../api/laborSkillApi';
import { LaborSkillForm } from '../components/LaborSkillForm';
import { LaborSkillTable } from '../components/LaborSkillTable';
import '../styles/MasterPageManagement.css';
import TopNav from '../components/TopNav';

const LaborSkillManagement = () => {
  const [laborSkills, setLaborSkills] = useState([]);
  const [filteredLaborSkills, setFilteredLaborSkills] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [currentLaborSkill, setCurrentLaborSkill] = useState(null);
  const [selectedIds, setSelectedIds] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    loadLaborSkills();
  }, []);

  useEffect(() => {
    const filtered = laborSkills.filter(skill =>
      skill.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredLaborSkills(filtered);
  }, [searchTerm, laborSkills]);

  const loadLaborSkills = async () => {
    try {
      const data = await fetchLaborSkills();
      setLaborSkills(data);
      setFilteredLaborSkills(data);
    } catch (error) {
      console.error('Error fetching labor skills:', error);
      toast.error('Failed to fetch labor skills');
    }
  };

  const handleSubmit = async (data) => {
    try {
      if (currentLaborSkill) {
        await updateLaborSkill({ ...data, id: currentLaborSkill.id });
        toast.success('Labor skill updated successfully');
      } else {
        await createLaborSkill(data);
        toast.success('New labor skill created successfully');
      }
      loadLaborSkills();
      setIsModalOpen(false);
      setCurrentLaborSkill(null);
    } catch (error) {
      console.error('Error submitting data:', error);
      toast.error('Failed to submit data');
    }
  };

  const handleEdit = (laborSkill) => {
    setCurrentLaborSkill(laborSkill);
    setIsModalOpen(true);
  };

  const handleDelete = async () => {
    if (currentLaborSkill) {
      try {
        await deleteLaborSkill(currentLaborSkill.id);
        toast.success('Labor skill deleted successfully');
        loadLaborSkills();
        setIsDeleteModalOpen(false);
        setCurrentLaborSkill(null);
      } catch (error) {
        console.error('Error deleting labor skill:', error);
        toast.error('Failed to delete labor skill');
      }
    }
  };

  const handleSelectAll = (checked) => {
    if (checked) {
      setSelectedIds(filteredLaborSkills.map(skill => skill.id));
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
      await Promise.all(selectedIds.map(id => deleteLaborSkill(id)));
      toast.success('Selected labor skills deleted successfully');
      loadLaborSkills();
      setSelectedIds([]);
    } catch (error) {
      console.error('Error deleting selected labor skills:', error);
      toast.error('Failed to delete selected labor skills');
    }
  };

  const openNewEntryModal = () => {
    setCurrentLaborSkill(null);
    setIsModalOpen(true);
  };

  const handleSearch = useCallback((term) => {
    setSearchTerm(term);
  }, []);

  return (
    <>
      <TopNav openNewEntryModal={openNewEntryModal} onSearch={handleSearch} />
      <div className="box">
        <div className="box-body">
          <div className="header-container">
            <h1 className="header-title">Labor Skill Management</h1>
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

          <LaborSkillTable
            laborSkills={filteredLaborSkills}
            onEdit={handleEdit}
            onDelete={(laborSkill) => {
              setCurrentLaborSkill(laborSkill);
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
                <h2 className="modal-title">{currentLaborSkill ? 'Edit' : 'New'} Labor Skill</h2>
                <LaborSkillForm
                  initialData={currentLaborSkill || undefined}
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
                <p>Are you sure you want to delete this labor skill?</p>
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

export default LaborSkillManagement;

