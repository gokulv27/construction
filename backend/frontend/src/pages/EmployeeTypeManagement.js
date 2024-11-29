import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import '../styles/EmployeeTypeManagement.css';

const API_BASE_URL = 'http://localhost:8000/masters/api/employeetypes/';

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

function EmployeeTypeManagement() {
  const [employeeTypes, setEmployeeTypes] = useState([]);
  const [formData, setFormData] = useState({ id: null, name: '', description: '' });
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    loadEmployeeTypes();
  }, []);

  const loadEmployeeTypes = async () => {
    try {
      const response = await axios.get(API_BASE_URL);
      setEmployeeTypes(response.data);
    } catch (error) {
      console.error('Error fetching employee types:', error);
      toast.error('Failed to fetch employee types');
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (isEditing) {
        await axios.put(`${API_BASE_URL}${formData.id}/update/`, formData);
        toast.success('Employee type updated successfully');
      } else {
        await axios.post(`${API_BASE_URL}create/`, formData);
        toast.success('New employee type created successfully');
      }
      loadEmployeeTypes();
      setIsModalOpen(false);
      resetForm();
    } catch (error) {
      console.error('Error submitting data:', error);
      toast.error('Failed to submit data');
    }
  };

  const handleEdit = (employeeType) => {
    setFormData(employeeType);
    setIsEditing(true);
    setIsModalOpen(true);
  };

  const handleDelete = async () => {
    try {
      await axios.delete(`${API_BASE_URL}${formData.id}/delete/`);
      toast.success('Employee type deleted successfully');
      loadEmployeeTypes();
      setIsDeleteModalOpen(false);
      resetForm();
    } catch (error) {
      console.error('Error deleting employee type:', error);
      toast.error('Failed to delete employee type');
    }
  };

  const resetForm = () => {
    setFormData({ id: null, name: '', description: '' });
    setIsEditing(false);
  };

  const openNewEntryModal = () => {
    resetForm();
    setIsModalOpen(true);
  };

  // Form Component
  const EmployeeTypeForm = () => (
    <form onSubmit={handleSubmit} className="form-container">
      <div className="form-group">
        <label htmlFor="name">Name</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleInputChange}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="description">Description</label>
        <textarea
          id="description"
          name="description"
          value={formData.description}
          onChange={handleInputChange}
          rows="3"
        />
      </div>
     
      <button type="submit" className="btn btn-primary">
        {isEditing ? 'Update' : 'Create'}
      </button>
    </form>
  );

  // Table Component
  const EmployeeTypeTable = () => (
    <table className="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Description</th>
          <th>Code</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {employeeTypes.length > 0 ? (
          employeeTypes.map((employeeType) => (
            <tr key={employeeType.id}>
              <td>{employeeType.id}</td>
              <td>{employeeType.name}</td>
              <td>{employeeType.description}</td>
              <td>{employeeType.code}</td>
              <td>
                <button onClick={() => handleEdit(employeeType)} className="btn btn-warning btn-sm">
                  Edit
                </button>
                <button onClick={() => {
                  setFormData(employeeType);
                  setIsDeleteModalOpen(true);
                }} className="btn btn-danger btn-sm">
                  Delete
                </button>
              </td>
            </tr>
          ))
        ) : (
          <tr>
            <td colSpan="5" className="text-center">
              No employee types available.
            </td>
          </tr>
        )}
      </tbody>
    </table>
  );

  // Modal Component
  const Modal = ({ isOpen, onClose, title, children }) => {
    if (!isOpen) return null;

    return (
      <div className="modal-overlay">
        <div className="modal">
          <div className="modal-header">
            <h2>{title}</h2>
            <button onClick={onClose} className="close-btn">&times;</button>
          </div>
          <div className="modal-content">
            {children}
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="employee-type-management">
      <h1>Employee Type Management</h1>
     

      <EmployeeTypeTable />

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={isEditing ? "Edit Employee Type" : "New Employee Type"}>
        <EmployeeTypeForm />
      </Modal>

      <Modal isOpen={isDeleteModalOpen} onClose={() => setIsDeleteModalOpen(false)} title="Confirm Deletion">
        <p>Are you sure you want to delete this employee type?</p>
        <button onClick={handleDelete} className="btn btn-danger">Delete</button>
        <button onClick={() => setIsDeleteModalOpen(false)} className="btn btn-secondary">Cancel</button>
      </Modal>

      <ToastContainer />
    </div>
  );
}

export default EmployeeTypeManagement;

