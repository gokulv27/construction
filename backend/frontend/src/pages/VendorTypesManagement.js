import React, { useState, useEffect, useCallback } from 'react';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { fetchVendorTypes, createVendorType, updateVendorType, deleteVendorType } from '../api/vendorTypeApi';
import { VendorTypeForm } from '../components/VendorTypeForm';
import { VendorTypeTable } from '../components/VendorTypeTable';
import '../styles/MasterPageManagement.css';
import TopNav from '../components/TopNav';

const VendorTypesManagement = () => {
  const [vendorTypes, setVendorTypes] = useState([]);
  const [filteredVendorTypes, setFilteredVendorTypes] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [currentVendorType, setCurrentVendorType] = useState(null);
  const [selectedIds, setSelectedIds] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    loadVendorTypes();
  }, []);

  useEffect(() => {
    const filtered = vendorTypes.filter(vt =>
      vt.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredVendorTypes(filtered);
  }, [searchTerm, vendorTypes]);

  const loadVendorTypes = async () => {
    try {
      const data = await fetchVendorTypes();
      setVendorTypes(data);
      setFilteredVendorTypes(data);
    } catch (error) {
      console.error('Error fetching vendor types:', error);
      toast.error('Failed to fetch vendor types');
    }
  };

  const handleSubmit = async (data) => {
    try {
      if (currentVendorType) {
        await updateVendorType({ ...data, id: currentVendorType.id });
        toast.success('Vendor type updated successfully');
      } else {
        await createVendorType(data);
        toast.success('New vendor type created successfully');
      }
      loadVendorTypes();
      setIsModalOpen(false);
      setCurrentVendorType(null);
    } catch (error) {
      console.error('Error submitting data:', error);
      toast.error('Failed to submit data');
    }
  };

  const handleEdit = (vendorType) => {
    setCurrentVendorType(vendorType);
    setIsModalOpen(true);
  };

  const handleDelete = async () => {
    if (currentVendorType) {
      try {
        await deleteVendorType(currentVendorType.id);
        toast.success('Vendor type deleted successfully');
        loadVendorTypes();
        setIsDeleteModalOpen(false);
        setCurrentVendorType(null);
      } catch (error) {
        console.error('Error deleting vendor type:', error);
        toast.error('Failed to delete vendor type');
      }
    }
  };

  const handleSelectAll = (checked) => {
    if (checked) {
      setSelectedIds(filteredVendorTypes.map(vt => vt.id));
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
      await Promise.all(selectedIds.map(id => deleteVendorType(id)));
      toast.success('Selected vendor types deleted successfully');
      loadVendorTypes();
      setSelectedIds([]);
    } catch (error) {
      console.error('Error deleting selected vendor types:', error);
      toast.error('Failed to delete selected vendor types');
    }
  };

  const openNewEntryModal = useCallback(() => {
    setCurrentVendorType(null);
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
            <h1 className="header-title">Vendor Type Management</h1>
            <button className="button" id="newEntryButton" onClick={openNewEntryModal}>
              <svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
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

          <VendorTypeTable
            vendorTypes={filteredVendorTypes}
            onEdit={handleEdit}
            onDelete={(vendorType) => {
              setCurrentVendorType(vendorType);
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
                <h2 className="modal-title">{currentVendorType ? 'Edit' : 'New'} Vendor Type</h2>
                <VendorTypeForm initialData={currentVendorType || undefined} onSubmit={handleSubmit} />
              </div>
            </div>
          )}

          {isDeleteModalOpen && (
            <div className="modal">
              <div className="modal-content">
                <span className="close" onClick={() => setIsDeleteModalOpen(false)}>&times;</span>
                <h2 className="modal-title">Confirm Deletion</h2>
                <p>Are you sure you want to delete this vendor type?</p>
                <div className="modal-actions">
                  <button onClick={handleDelete} className="btn btn-danger">Delete</button>
                  <button onClick={() => setIsDeleteModalOpen(false)} className="btn btn-secondary">Cancel</button>
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

export default VendorTypesManagement;
