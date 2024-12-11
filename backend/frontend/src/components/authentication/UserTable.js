import React from 'react';
import '../../styles/MasterPageManagement.css';
import { deleteUser } from '../../api/userApi';

export const UserTable = ({ users, onEdit, onDelete, onSelectAll, onSelectOne, selectedIds }) => {
  const handleDelete = async (user) => {
    try {
      await deleteUser(user.id); // Call API to delete user
      if (onDelete) onDelete(user); // Trigger external callback if provided
    } catch (error) {
      console.error('Error deleting user:', error);
    }
  };

  return (
    <table className="table">
      <thead>
        <tr>
          <th>
            <label className="checkbox-wrapper">
              <input
                type="checkbox"
                onChange={(e) => onSelectAll(e.target.checked)}
                checked={selectedIds.length === users.length && users.length > 0}
              />
              <span className="checkmark"></span>
            </label>
          </th>
          <th>ID</th>
          <th>Name</th>
          <th>Username</th>
          <th>Role</th>
          <th>Status</th>
          <th>Created By</th>
          <th>Created At</th>
          <th>Updated By</th>
          <th>Updated At</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {users.map((user) => (
          <tr key={user.id}>
            <td>
              <label className="checkbox-wrapper">
                <input
                  type="checkbox"
                  onChange={(e) => onSelectOne(user.id, e.target.checked)}
                  checked={selectedIds.includes(user.id)}
                />
                <span className="checkmark"></span>
              </label>
            </td>
            <td>{user.id}</td>
            <td>{user.name}</td>
            <td>{user.username}</td>
            <td>{user.role}</td>
            <td>{user.status}</td>
            <td>{user.created_by || 'N/A'}</td>
            <td>{user.created_at || 'N/A'}</td>
            <td>{user.updated_by || 'N/A'}</td>
            <td>{user.updated_at || 'N/A'}</td>
            <td>
              <button onClick={() => onEdit(user)} className="btn btn-warning btn-sm mr-2">
                Edit
              </button>
              <button onClick={() => handleDelete(user)} className="btn btn-danger btn-sm">
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
