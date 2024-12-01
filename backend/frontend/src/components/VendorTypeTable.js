import React from 'react';
import '../styles/MasterPageManagement.css'; // Updated CSS import

export const VendorTypeTable = ({ vendorTypes, onEdit, onDelete, onSelectAll, onSelectOne, selectedIds }) => {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>
            <label className="checkbox-wrapper">
              <input
                type="checkbox"
                onChange={(e) => onSelectAll(e.target.checked)}
                checked={selectedIds.length === vendorTypes.length && vendorTypes.length > 0}
              />
              <span className="checkmark"></span>
            </label>
          </th>
          <th>ID</th>
          <th>Name</th>
          <th>Created At</th>
          <th>Updated At</th>
          <th>Created By</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {vendorTypes.map((vendorType) => (
          <tr key={vendorType.id}>
            <td>
              <label className="checkbox-wrapper">
                <input
                  type="checkbox"
                  onChange={(e) => onSelectOne(vendorType.id, e.target.checked)}
                  checked={selectedIds.includes(vendorType.id)}
                />
                <span className="checkmark"></span>
              </label>
            </td>
            <td>{vendorType.id}</td>
            <td>{vendorType.name}</td>
            <td>{vendorType.created_at || 'N/A'}</td>
            <td>{vendorType.updated_at || 'N/A'}</td>
            <td>{vendorType.created_by || 'N/A'}</td>
            <td>
              <button onClick={() => onEdit(vendorType)} className="btn btn-warning btn-sm mr-2">
                Edit
              </button>
              <button onClick={() => onDelete(vendorType)} className="btn btn-danger btn-sm">
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
