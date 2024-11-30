import React, { useState, useEffect } from 'react';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { fetchEmployeeTypes, createEmployeeType, updateEmployeeType, deleteEmployeeType } from '../api/employeeTypeApi';
import { EmployeeTypeForm } from '../components/EmployeeTypeForm';
import { EmployeeTypeTable } from '../components/EmployeeTypeTable';
import '../styles/EmployeeTypeManagement.css'

export const EmployeeTypeManagement = () => {
  const [employeeTypes, setEmployeeTypes] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [currentEmployeeType, setCurrentEmployeeType] = useState(null);

  useEffect(() => {
    loadEmployeeTypes();
  }, []);

  const loadEmployeeTypes = async () => {
    try {
      const data = await fetchEmployeeTypes();
      setEmployeeTypes(data);
    } catch (error) {
      console.error('Error fetching employee types:', error);
      toast.error('Failed to fetch employee types');
    }
  };

  const handleSubmit = async (data) => {
    try {
      if (currentEmployeeType) {
        await updateEmployeeType({ ...data, id: currentEmployeeType.id });
        toast.success('Employee type updated successfully');
      } else {
        await createEmployeeType(data);
        toast.success('New employee type created successfully');
      }
      loadEmployeeTypes();
      setIsModalOpen(false);
      setCurrentEmployeeType(null);
    } catch (error) {
      console.error('Error submitting data:', error);
      toast.error('Failed to submit data');
    }
  };

  const handleEdit = (employeeType) => {
    setCurrentEmployeeType(employeeType);
    setIsModalOpen(true);
  };

  const handleDelete = async () => {
    if (currentEmployeeType) {
      try {
        await deleteEmployeeType(currentEmployeeType.id);
        toast.success('Employee type deleted successfully');
        loadEmployeeTypes();
        setIsDeleteModalOpen(false);
        setCurrentEmployeeType(null);
      } catch (error) {
        console.error('Error deleting employee type:', error);
        toast.error('Failed to delete employee type');
      }
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Employee Type Management</h1>
        <button
          onClick={() => setIsModalOpen(true)}
          className="px-4 py-2 bg-gray-800 text-white rounded hover:bg-gray-700"
        >
          Add New Employee Type
        </button>
      </div>

      <EmployeeTypeTable
        employeeTypes={employeeTypes}
        onEdit={handleEdit}
        onDelete={(employeeType) => {
          setCurrentEmployeeType(employeeType);
          setIsDeleteModalOpen(true);
        }}
      />

      {isModalOpen && (
        <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full">
          <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
            <h2 className="text-xl font-bold mb-4">{currentEmployeeType ? 'Edit' : 'New'} Employee Type</h2>
            <EmployeeTypeForm
              initialData={currentEmployeeType || undefined}
              onSubmit={handleSubmit}
            />
            <button
              onClick={() => {
                setIsModalOpen(false);
                setCurrentEmployeeType(null);
              }}
              className="mt-4 px-4 py-2 bg-gray-200 text-gray-800 rounded hover:bg-gray-300"
            >
              Cancel
            </button>
          </div>
        </div>
      )}

      {isDeleteModalOpen && (
        <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full">
          <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
            <h2 className="text-xl font-bold mb-4">Confirm Deletion</h2>
            <p>Are you sure you want to delete this employee type?</p>
            <div className="mt-4">
              <button
                onClick={handleDelete}
                className="px-4 py-2 bg-gray-800 text-white rounded hover:bg-gray-700 mr-2"
              >
                Delete
              </button>
              <button
                onClick={() => setIsDeleteModalOpen(false)}
                className="px-4 py-2 bg-gray-200 text-gray-800 rounded hover:bg-gray-300"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}

      <ToastContainer />
    </div>
  );
};

export default EmployeeTypeManagement;