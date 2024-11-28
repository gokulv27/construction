import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/masters/api/employeetypes/';

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export const fetchEmployeeTypes = async () => {
  try {
    const response = await axios.get(API_BASE_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching employee types:', error);
    throw error;
  }
};

export const createEmployeeType = async (employeeType) => {
  try {
    const response = await axios.post(`${API_BASE_URL}create/`, employeeType);
    return response.data;
  } catch (error) {
    console.error('Error creating employee type:', error);
    throw error;
  }
};

export const updateEmployeeType = async (id, updatedData) => {
  try {
    const response = await axios.put(`${API_BASE_URL}${id}/update/`, updatedData);
    return response.data;
  } catch (error) {
    console.error('Error updating employee type:', error);
    throw error;
  }
};

export const deleteEmployeeType = async (id) => {
  try {
    const response = await axios.delete(`${API_BASE_URL}${id}/delete/`);
    return response.data;
  } catch (error) {
    console.error('Error deleting employee type:', error);
    throw error;
  }
};

