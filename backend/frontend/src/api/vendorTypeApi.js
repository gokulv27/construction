import axios from 'axios';

// Base URL for the vendor-types API
const API_BASE_URL = 'http://127.0.0.1:8000/masters/api/vendor-types/';

// Set up CSRF token headers for Django compatibility
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

// Fetch all vendor types
export const fetchVendorTypes = async () => {
  const response = await axios.get(API_BASE_URL);
  return response.data;
};

// Create a new vendor type
export const createVendorType = async (data) => {
  const response = await axios.post(`${API_BASE_URL}create/`, data);
  return response.data;
};

// Update an existing vendor type by ID
export const updateVendorType = async (data) => {
  const response = await axios.put(`${API_BASE_URL}${data.id}/update/`, data);
  return response.data;
};

// Delete a vendor type by ID
export const deleteVendorType = async (id) => {
  await axios.delete(`${API_BASE_URL}${id}/delete/`);
};
