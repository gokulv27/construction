
import React from 'react';
import '../styles/MasterPageManagement.css'; // Updated CSS import

export const DocumentTypeTable = ({ documentTypes, onEdit, onDelete, onSelectAll, onSelectOne, selectedIds }) => {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>
            <label className="checkbox-wrapper">
              <input
                type="checkbox"
                onChange={(e) => onSelectAll(e.target.checked)}
                checked={selectedIds.length === documentTypes.length && documentTypes.length > 0}
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
        {documentTypes.map((documentType) => (
          <tr key={documentType.id}>
            <td>
              <label className="checkbox-wrapper">
                <input
                  type="checkbox"
                  onChange={(e) => onSelectOne(documentType.id, e.target.checked)}
                  checked={selectedIds.includes(documentType.id)}
                />
                <span className="checkmark"></span>
              </label>
            </td>
            <td>{documentType.id}</td>
            <td>{documentType.name}</td>
            <td>{documentType.created_at || 'N/A'}</td>
            <td>{documentType.updated_at || 'N/A'}</td>
            <td>{documentType.created_by || 'N/A'}</td>
            <td>
              <button onClick={() => onEdit(documentType)} className="btn btn-warning btn-sm mr-2">
                Edit
              </button>
              <button onClick={() => onDelete(documentType)} className="btn btn-danger btn-sm">
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};