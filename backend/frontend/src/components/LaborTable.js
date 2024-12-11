import React from 'react';
import '../styles/labor.css';

export const LaborTable = ({ labors, onEdit, onDelete, onSelectAll, onSelectOne, selectedIds }) => {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>
            <label className="checkbox-wrapper">
              <input
                type="checkbox"
                onChange={(e) => onSelectAll(e.target.checked)}
                checked={selectedIds.length === labors.length && labors.length > 0}
              />
              <span className="checkmark"></span>
            </label>
          </th>
          <th>ID</th>
          <th>Name</th>
          <th>Phone Number</th>
          <th>Aadhar Number</th>
          <th>Emergency Contact</th>
          <th>Address</th>
          <th>City</th>
          <th>State</th>
          <th>Pincode</th>
          <th>Daily Wages</th>
          <th>Created At</th>
          <th>Updated At</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {labors.map((labor) => (
          <tr key={labor.id}>
            <td>
              <label className="checkbox-wrapper">
                <input
                  type="checkbox"
                  onChange={(e) => onSelectOne(labor.id, e.target.checked)}
                  checked={selectedIds.includes(labor.id)}
                />
                <span className="checkmark"></span>
              </label>
            </td>
            <td>{labor.id}</td>
            <td>{labor.name}</td>
            <td>{labor.phone_no}</td>
            <td>{labor.aadhar_no}</td>
            <td>{labor.emergency_contact_number}</td>
            <td>{labor.address}</td>
            <td>{labor.city}</td>
            <td>{labor.state}</td>
            <td>{labor.pincode}</td>
            <td>{labor.daily_wages}</td>
            <td>{labor.created_at}</td>
            <td>{labor.updated_at}</td>
            <td>
              <button onClick={() => onEdit(labor)} className="btn btn-warning btn-sm mr-2">
                Edit
              </button>
              <button onClick={() => onDelete(labor)} className="btn btn-danger btn-sm">
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

