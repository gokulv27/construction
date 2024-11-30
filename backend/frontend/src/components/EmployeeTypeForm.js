import React from 'react';
import { useForm } from 'react-hook-form';
import '../styles/EmployeeTypeManagement.css'


export const EmployeeTypeForm = ({ initialData, onSubmit }) => {
  const { register, handleSubmit, formState: { errors } } = useForm({
    defaultValues: initialData,
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div>
        <label htmlFor="name" className="block text-sm font-medium text-gray-700">Name</label>
        <input
          type="text"
          id="name"
          {...register('name', { required: 'Name is required' })}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-gray-500 focus:ring focus:ring-gray-200 focus:ring-opacity-50"
        />
        {errors.name && <p className="mt-1 text-sm text-red-600">{errors.name.message}</p>}
      </div>
      <button type="submit" className="px-4 py-2 bg-gray-800 text-white rounded hover:bg-gray-700">
        {initialData ? 'Update' : 'Create'}
      </button>
    </form>
  );
};

