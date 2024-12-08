import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/masters/api/labor-skills/';

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

// Fetch all labor skills
export const fetchLaborSkills = async () => {
  const response = await axios.get(API_BASE_URL);
  return response.data;
};

// Create a new labor skill
export const createLaborSkill = async (skillData) => {
  const response = await axios.post(`${API_BASE_URL}create/`, skillData);
  return response.data;
};

// Update an existing labor skill
export const updateLaborSkill = async (skillData) => {
  const response = await axios.put(`${API_BASE_URL}update/${skillData.id}/`, skillData);
  return response.data;
};

// Delete a labor skill
export const deleteLaborSkill = async (id) => {
  await axios.delete(`${API_BASE_URL}delete/${id}/`);
};

