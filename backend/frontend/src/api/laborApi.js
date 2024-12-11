import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/labour_management/api/labors/';

// Set up CSRF token handling
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export const fetchLabors = async () => {
    const response = await axios.get(API_BASE_URL);
    return response.data;
};

export const createLabor = async (laborData) => {
    const response = await axios.post(`${API_BASE_URL}create/`, data);
    return response.data;
};

export const updateLabor = async (id, laborData) => {
    const response = await axios.put(`${API_BASE_URL}${data.id}/update/`, data);
    return response.data;
};

export const deleteLabor = async (id) => {
    await axios.delete(`${API_BASE_URL}${id}/delete/`);
};

export const getCSRFToken = () => {
  return axios.get(`${API_BASE_URL}`).then(response => response.data.csrfToken);
};

