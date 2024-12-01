import React from 'react';
import { useForm } from 'react-hook-form';
import '../styles/MasterPageManagement.css'; // Updated CSS import

export const DocumentTypeForm = ({ initialData, onSubmit }) => {
  const { register, handleSubmit, formState: { errors } } = useForm({
    defaultValues: initialData,
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
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
      <button type="submit" className="btn btn-primary">
        {initialData ? 'Update' : 'Create'}
      </button>
    </form>
  );
};