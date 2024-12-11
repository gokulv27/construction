import axios from 'axios';

// Base URL for API endpoints
const API_BASE_URL = 'http://127.0.0.1:8000/masters/api/labor-skills/';

// Configure CSRF tokens for Django
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

// Fetch all labor skills
export const fetchLaborSkills = async () => {
  try {
    const response = await axios.get(API_BASE_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching labor skills:', error);
    throw error;
  }
};

// Create a new labor skill
export const createLaborSkill = async (skillData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}`, skillData);
    return response.data;
  } catch (error) {
    console.error('Error creating labor skill:', error);
    throw error;
  }
};

// Update an existing labor skill
export const updateLaborSkill = async (id, skillData) => {
  try {
    const response = await axios.put(`${API_BASE_URL}${id}/update/`, skillData);
    return response.data;
  } catch (error) {
    console.error(`Error updating labor skill with id ${id}:`, error);
    throw error;
  }
};

// Delete a labor skill
export const deleteLaborSkill = async (id) => {
  try {
    const response = await axios.delete(`${API_BASE_URL}${id}/delete/`);
    return response.data;
  } catch (error) {
    console.error(`Error deleting labor skill with id ${id}:`, error);
    throw error;
  }
};
