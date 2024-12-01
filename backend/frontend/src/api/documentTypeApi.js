import axios from 'axios';

// Base URL for the document-types API
const API_BASE_URL = 'http://127.0.0.1:8000/masters/api/document-types/';

// Set up CSRF token headers for Django compatibility
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

// Fetch all document types
export const fetchDocumentTypes = async () => {
  const response = await axios.get(API_BASE_URL);
  return response.data;
};

// Create a new document type
export const createDocumentType = async (data) => {
  const response = await axios.post(`${API_BASE_URL}create/`, data);
  return response.data;
};

// Update an existing document type by ID
export const updateDocumentType = async (data) => {
  const response = await axios.put(`${API_BASE_URL}update/${data.id}/`, data);
  return response.data;
};

// Delete a document type by ID
export const deleteDocumentType = async (id) => {
  await axios.delete(`${API_BASE_URL}delete/${id}/`);
};
