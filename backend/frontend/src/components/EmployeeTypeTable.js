import React from 'react';
import '../styles/EmployeeTypeManagement.css'

export const EmployeeTypeTable = ({ employeeTypes, onEdit, onDelete }) => {
  return (
    <table className="min-w-full divide-y divide-gray-200">
      <thead className="bg-gray-50">
        <tr>
          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Created At</th>
          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Updated At</th>
          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Created By</th>
          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
        </tr>
      </thead>
      <tbody className="bg-white divide-y divide-gray-200">
        {employeeTypes.map((employeeType) => (
          <tr key={employeeType.id}>
            <td className="px-6 py-4 whitespace-nowrap">{employeeType.id}</td>
            <td className="px-6 py-4 whitespace-nowrap">{employeeType.name}</td>
            <td className="px-6 py-4 whitespace-nowrap">{employeeType.created_at || 'N/A'}</td>
            <td className="px-6 py-4 whitespace-nowrap">{employeeType.updated_at || 'N/A'}</td>
            <td className="px-6 py-4 whitespace-nowrap">{employeeType.created_by || 'N/A'}</td>
            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
              <button onClick={() => onEdit(employeeType)} className="text-gray-600 hover:text-gray-900 mr-2">
                Edit
              </button>
              <button onClick={() => onDelete(employeeType)} className="text-gray-600 hover:text-gray-900">
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

