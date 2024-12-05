import React, { useState, useEffect, useCallback } from 'react';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { fetchUsers, createUser, updateUser, deleteUser } from '../api/userApi';
import { AddUserForm } from '../components/authentication/UserForm';
import { UserTable } from '../components/authentication/UserTable';
import '../styles/MasterPageManagement.css';
import TopNav from '../components/TopNav';

const UserManagement = () => {
  const [users, setUsers] = useState([]);
  const [filteredUsers, setFilteredUsers] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [currentUser, setCurrentUser] = useState(null);
  const [selectedIds, setSelectedIds] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    loadUsers();
  }, []);

  useEffect(() => {
    const filtered = users.filter(user =>
      user.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredUsers(filtered);
  }, [searchTerm, users]);

  const loadUsers = async () => {
    try {
      const data = await fetchUsers();
      setUsers(data);
      setFilteredUsers(data);
    } catch (error) {
      console.error('Error fetching users:', error);
      toast.error('Failed to fetch users');
    }
  };

  const handleSubmit = async (data) => {
    try {
      if (currentUser) {
        await updateUser({ ...data, id: currentUser.id });
        toast.success('User updated successfully');
      } else {
        await createUser(data);
        toast.success('New user created successfully');
      }
      loadUsers();
      setIsModalOpen(false);
      setCurrentUser(null);
    } catch (error) {
      console.error('Error submitting data:', error);
      toast.error('Failed to submit data');
    }
  };

  const handleEdit = (user) => {
    setCurrentUser(user);
    setIsModalOpen(true);
  };

  const handleDelete = async () => {
    if (currentUser) {
      try {
        await deleteUser(currentUser.id);
        toast.success('User deleted successfully');
        loadUsers();
        setIsDeleteModalOpen(false);
        setCurrentUser(null);
      } catch (error) {
        console.error('Error deleting user:', error);
        toast.error('Failed to delete user');
      }
    }
  };

  const handleSelectAll = (checked) => {
    if (checked) {
      setSelectedIds(filteredUsers.map(user => user.id));
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
      await Promise.all(selectedIds.map(id => deleteUser(id)));
      toast.success('Selected users deleted successfully');
      loadUsers();
      setSelectedIds([]);
    } catch (error) {
      console.error('Error deleting selected users:', error);
      toast.error('Failed to delete selected users');
    }
  };

  const openNewEntryModal = useCallback(() => {
    setCurrentUser(null);
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
            <h1 className="header-title">User Management</h1>
            <button className="button" id="newEntryButton" onClick={openNewEntryModal}>
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
              New User
            </button>
          </div>

          {selectedIds.length > 0 && (
            <div className="mb-4">
              <button onClick={handleDeleteSelected} className="btn btn-danger">
                Delete Selected ({selectedIds.length})
              </button>
            </div>
          )}

          <UserTable
            users={filteredUsers}
            onEdit={handleEdit}
            onDelete={(user) => {
              setCurrentUser(user);
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
                <h2 className="modal-title">{currentUser ? 'Edit' : 'New'} User</h2>
                <AddUserForm initialData={currentUser || undefined} onSubmit={handleSubmit} />
              </div>
            </div>
          )}

          {isDeleteModalOpen && (
            <div className="modal">
              <div className="modal-content">
                <span className="close" onClick={() => setIsDeleteModalOpen(false)}>&times;</span>
                <h2 className="modal-title">Confirm Deletion</h2>
                <p>Are you sure you want to delete this user?</p>
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

export default UserManagement;
