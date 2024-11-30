import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/masters/api/employee-types/';

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export const fetchEmployeeTypes = async () => {
  const response = await axios.get(API_BASE_URL);
  return response.data;
};

export const createEmployeeType = async (data) => {
  const response = await axios.post(`${API_BASE_URL}create/`, data);
  return response.data;
};

export const updateEmployeeType = async (data) => {
  const response = await axios.put(`${API_BASE_URL}update/${data.id}/`, data);
  return response.data;
};

export const deleteEmployeeType = async (id) => {
  await axios.delete(`${API_BASE_URL}delete/${id}/`);
};

