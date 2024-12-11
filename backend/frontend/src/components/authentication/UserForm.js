import React from 'react';
import { useForm } from 'react-hook-form';
import '../../styles/MasterPageManagement.css';
import { createUser, updateUser } from '../../api/userApi';

export const AddUserForm = ({ initialData, onSubmit }) => {
  const { register, handleSubmit, formState: { errors } } = useForm({
    defaultValues: initialData,
  });

  const handleFormSubmit = async (data) => {
    try {
      if (initialData) {
        // Update user
        await updateUser({ ...initialData, ...data });
      } else {
        // Create new user
        await createUser(data);
      }
      if (onSubmit) onSubmit(); // Trigger callback if provided
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit(handleFormSubmit)} className="space-y-4">
      <div className="form-group">
        <label htmlFor="name" className="block text-sm font-medium text-gray-700">Name</label>
        <input
          type="text"
          id="name"
          {...register('name', { required: 'Name is required' })}
          className="form-control"
        />
        {errors.name && <p className="mt-1 text-sm text-red-600">{errors.name.message}</p>}
      </div>

      <div className="form-group">
        <label htmlFor="username" className="block text-sm font-medium text-gray-700">Username</label>
        <input
          type="text"
          id="username"
          {...register('username', { required: 'Username is required' })}
          className="form-control"
        />
        {errors.username && <p className="mt-1 text-sm text-red-600">{errors.username.message}</p>}
      </div>

      <div className="form-group">
        <label htmlFor="role" className="block text-sm font-medium text-gray-700">Role</label>
        <input
          type="text"
          id="role"
          {...register('role', { required: 'Role is required' })}
          className="form-control"
        />
        {errors.role && <p className="mt-1 text-sm text-red-600">{errors.role.message}</p>}
      </div>

      <button type="submit" className="btn btn-primary">
        {initialData ? 'Update' : 'Create'}
      </button>
    </form>
  );
};
