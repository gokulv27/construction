import React from 'react';
import '../styles/MasterPageManagement.css';

export const LaborSkillTable = ({ laborSkills, onEdit, onDelete, onSelectAll, onSelectOne, selectedIds }) => {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>
            <label className="checkbox-wrapper">
              <input
                type="checkbox"
                onChange={(e) => onSelectAll(e.target.checked)}
                checked={selectedIds.length === laborSkills.length && laborSkills.length > 0}
              />
              <span className="checkmark"></span>
            </label>
          </th>
          <th>ID</th>
          <th>Name</th>
          <th>Created At</th>
          <th>Updated At</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {laborSkills.map((laborSkill) => (
          <tr key={laborSkill.id}>
            <td>
              <label className="checkbox-wrapper">
                <input
                  type="checkbox"
                  onChange={(e) => onSelectOne(laborSkill.id, e.target.checked)}
                  checked={selectedIds.includes(laborSkill.id)}
                />
                <span className="checkmark"></span>
              </label>
            </td>
            <td>{laborSkill.id}</td>
            <td>{laborSkill.name}</td>
            <td>{laborSkill.created_at || 'N/A'}</td>
            <td>{laborSkill.updated_at || 'N/A'}</td>
            <td>
              <button onClick={() => onEdit(laborSkill)} className="btn btn-warning btn-sm mr-2">
                Edit
              </button>
              <button onClick={() => onDelete(laborSkill)} className="btn btn-danger btn-sm">
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
