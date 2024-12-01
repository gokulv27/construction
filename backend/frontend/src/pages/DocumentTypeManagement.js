import React, { useState, useEffect, useCallback } from 'react';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { fetchDocumentTypes, createDocumentType, updateDocumentType, deleteDocumentType } from '../api/documentTypeApi';
import { DocumentTypeForm } from '../components/DocumentTypeForm';
import { DocumentTypeTable } from '../components/DocumentTypeTable';
import '../styles/MasterPageManagement.css';
import TopNav from '../components/TopNav';

const DocumentTypeManagement = () => {
  const [documentTypes, setDocumentTypes] = useState([]);
  const [filteredDocumentTypes, setFilteredDocumentTypes] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [currentDocumentType, setCurrentDocumentType] = useState(null);
  const [selectedIds, setSelectedIds] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    loadDocumentTypes();
  }, []);

  useEffect(() => {
    const filtered = documentTypes.filter(dt =>
      dt.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredDocumentTypes(filtered);
  }, [searchTerm, documentTypes]);

  const loadDocumentTypes = async () => {
    try {
      const data = await fetchDocumentTypes();
      setDocumentTypes(data);
      setFilteredDocumentTypes(data);
    } catch (error) {
      console.error('Error fetching document types:', error);
      toast.error('Failed to fetch document types');
    }
  };

  const handleSubmit = async (data) => {
    try {
      if (currentDocumentType) {
        await updateDocumentType({ ...data, id: currentDocumentType.id });
        toast.success('Document type updated successfully');
      } else {
        await createDocumentType(data);
        toast.success('New document type created successfully');
      }
      loadDocumentTypes();
      setIsModalOpen(false);
      setCurrentDocumentType(null);
    } catch (error) {
      console.error('Error submitting data:', error);
      toast.error('Failed to submit data');
    }
  };

  const handleEdit = (documentType) => {
    setCurrentDocumentType(documentType);
    setIsModalOpen(true);
  };

  const handleDelete = async () => {
    if (currentDocumentType) {
      try {
        await deleteDocumentType(currentDocumentType.id);
        toast.success('Document type deleted successfully');
        loadDocumentTypes();
        setIsDeleteModalOpen(false);
        setCurrentDocumentType(null);
      } catch (error) {
        console.error('Error deleting document type:', error);
        toast.error('Failed to delete document type');
      }
    }
  };

  const handleSelectAll = (checked) => {
    if (checked) {
      setSelectedIds(filteredDocumentTypes.map(dt => dt.id));
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
      await Promise.all(selectedIds.map(id => deleteDocumentType(id)));
      toast.success('Selected document types deleted successfully');
      loadDocumentTypes();
      setSelectedIds([]);
    } catch (error) {
      console.error('Error deleting selected document types:', error);
      toast.error('Failed to delete selected document types');
    }
  };

  const openNewEntryModal = useCallback(() => {
    setCurrentDocumentType(null);
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
            <h1 className="header-title">Document Type Management</h1>
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

          <DocumentTypeTable
            documentTypes={filteredDocumentTypes}
            onEdit={handleEdit}
            onDelete={(documentType) => {
              setCurrentDocumentType(documentType);
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
                <h2 className="modal-title">{currentDocumentType ? 'Edit' : 'New'} Document Type</h2>
                <DocumentTypeForm initialData={currentDocumentType || undefined} onSubmit={handleSubmit} />
              </div>
            </div>
          )}

          {isDeleteModalOpen && (
            <div className="modal">
              <div className="modal-content">
                <span className="close" onClick={() => setIsDeleteModalOpen(false)}>&times;</span>
                <h2 className="modal-title">Confirm Deletion</h2>
                <p>Are you sure you want to delete this document type?</p>
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

export default DocumentTypeManagement;
