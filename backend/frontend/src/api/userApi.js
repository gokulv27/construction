import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/authentication/users/';

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export const fetchUsers = async () => {
  const response = await axios.get(API_BASE_URL);
  return response.data.results; // Extract 'results' from API response
};

export const createUser = async (data) => {
  const response = await axios.post(`${API_BASE_URL}create/`, data);
  return response.data;
};

export const updateUser = async (data) => {
  const response = await axios.put(`${API_BASE_URL}update/${data.id}/`, data);
  return response.data;
};

export const deleteUser = async (id) => {
  await axios.delete(`${API_BASE_URL}delete/${id}/`);
};

export const fetchUserDetails = async (id) => {
  const response = await axios.get(`${API_BASE_URL}${id}/`);
  return response.data;
};
