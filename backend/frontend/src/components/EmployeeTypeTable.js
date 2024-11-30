import React from 'react';
import '../styles/EmployeeTypeManagement.css';

export const EmployeeTypeTable = ({ employeeTypes, onEdit, onDelete, onSelectAll, onSelectOne, selectedIds }) => {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>
            <label className="checkbox-wrapper">
              <input
                type="checkbox"
                onChange={(e) => onSelectAll(e.target.checked)}
                checked={selectedIds.length === employeeTypes.length && employeeTypes.length > 0}
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
        {employeeTypes.map((employeeType) => (
          <tr key={employeeType.id}>
            <td>
              <label className="checkbox-wrapper">
                <input
                  type="checkbox"
                  onChange={(e) => onSelectOne(employeeType.id, e.target.checked)}
                  checked={selectedIds.includes(employeeType.id)}
                />
                <span className="checkmark"></span>
              </label>
            </td>
            <td>{employeeType.id}</td>
            <td>{employeeType.name}</td>
            <td>{employeeType.created_at || 'N/A'}</td>
            <td>{employeeType.updated_at || 'N/A'}</td>
            <td>{employeeType.created_by || 'N/A'}</td>
            <td>
              <button onClick={() => onEdit(employeeType)} className="btn btn-warning btn-sm mr-2">
                Edit
              </button>
              <button onClick={() => onDelete(employeeType)} className="btn btn-danger btn-sm">
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

