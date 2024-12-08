import React from 'react';

export const LaborForm = ({ initialData, onSubmit }) => {
  const [formData, setFormData] = React.useState(initialData);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevData => ({
      ...prevData,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="name" className="block text-sm font-medium text-gray-700">Name</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name || ''}
          onChange={handleChange}
          required
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
      </div>

      <div>
        <label htmlFor="phone_no" className="block text-sm font-medium text-gray-700">Phone Number</label>
        <input
          type="tel"
          id="phone_no"
          name="phone_no"
          value={formData.phone_no || ''}
          onChange={handleChange}
          required
          maxLength={15}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
      </div>

      <div>
        <label htmlFor="aadhar_no" className="block text-sm font-medium text-gray-700">Aadhar Number</label>
        <input
          type="text"
          id="aadhar_no"
          name="aadhar_no"
          value={formData.aadhar_no || ''}
          onChange={handleChange}
          required
          maxLength={12}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
      </div>

      <div>
        <label htmlFor="emergency_contact_number" className="block text-sm font-medium text-gray-700">Emergency Contact Number</label>
        <input
          type="tel"
          id="emergency_contact_number"
          name="emergency_contact_number"
          value={formData.emergency_contact_number || ''}
          onChange={handleChange}
          required
          maxLength={15}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
      </div>

      <div>
        <label htmlFor="address" className="block text-sm font-medium text-gray-700">Address</label>
        <textarea
          id="address"
          name="address"
          value={formData.address || ''}
          onChange={handleChange}
          required
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
      </div>

      <div>
        <label htmlFor="city" className="block text-sm font-medium text-gray-700">City</label>
        <input
          type="text"
          id="city"
          name="city"
          value={formData.city || ''}
          onChange={handleChange}
          required
          maxLength={30}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
      </div>

      <div>
        <label htmlFor="state" className="block text-sm font-medium text-gray-700">State</label>
        <input
          type="text"
          id="state"
          name="state"
          value={formData.state || ''}
          onChange={handleChange}
          required
          maxLength={30}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
      </div>

      <div>
        <label htmlFor="pincode" className="block text-sm font-medium text-gray-700">Pincode</label>
        <input
          type="text"
          id="pincode"
          name="pincode"
          value={formData.pincode || ''}
          onChange={handleChange}
          required
          maxLength={6}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
      </div>

      <div>
        <label htmlFor="daily_wages" className="block text-sm font-medium text-gray-700">Daily Wages</label>
        <input
          type="number"
          id="daily_wages"
          name="daily_wages"
          value={formData.daily_wages || ''}
          onChange={handleChange}
          required
          step="0.01"
          min="0"
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
      </div>

      <button type="submit" className="w-full px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        Submit
      </button>
    </form>
  );
};

