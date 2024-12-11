"use client";

import React, { useState } from "react";
import { createUser } from '../../api/userApi'; // Adjust the path if needed
import styles from "../../styles/createcustomer.css";

export default function AddUser() {
  const [formData, setFormData] = useState({
    name: "",
    username: "",
    email: "",
    phoneNumber: "",
    password: "",
    role: "Client",
    status: "Active",
    country: "",
    address: "",
    city: "",
    postalCode: "",
    created_by: "current_user", // Replace with actual user data if available
    updated_by: "current_user", // Replace with actual user data if available
  });

  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setSuccess(null);

    try {
      const response = await createUser(formData);
      console.log("User created:", response);
      setSuccess("User created successfully!");
      setFormData({
        name: "",
        username: "",
        email: "",
        phoneNumber: "",
        password: "",
        role: "Client",
        status: "Active",
        country: "",
        address: "",
        city: "",
        postalCode: "",
        created_by: "current_user", // Reset
        updated_by: "current_user", // Reset
      }); // Reset form
    } catch (err) {
      setError(err.response?.data?.detail || "An error occurred.");
    }
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Create Customer</h1>
      <form onSubmit={handleSubmit}>
        <div className={styles.grid}>
          <div className={styles.mainContent}>
            <div className={styles.card}>
              <h2 className={styles.cardTitle}>Overview</h2>
              <div className={styles.cardContent}>
                <div className={styles.twoColumnGrid}>
                  <div>
                    <label htmlFor="name" className={styles.label}>
                      First Name
                    </label>
                    <input
                      type="text"
                      id="name"
                      name="name"
                      value={formData.name}
                      onChange={handleChange}
                      className={styles.input}
                    />
                  </div>
                  <div>
                    <label htmlFor="username" className={styles.label}>
                      User Name
                    </label>
                    <input
                      type="text"
                      id="username"
                      name="username"
                      value={formData.username}
                      onChange={handleChange}
                      className={styles.input}
                    />
                  </div>
                </div>
                <div>
                  <label htmlFor="email" className={styles.label}>
                    Email
                  </label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    className={styles.input}
                  />
                </div>
                <div>
                  <label htmlFor="phoneNumber" className={styles.label}>
                    Phone Number
                  </label>
                  <input
                    type="tel"
                    id="phoneNumber"
                    name="phoneNumber"
                    value={formData.phoneNumber}
                    onChange={handleChange}
                    className={styles.input}
                  />
                </div>
                <div>
                  <label htmlFor="password" className={styles.label}>
                    Password
                  </label>
                  <input
                    type="password"
                    id="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    className={styles.input}
                  />
                </div>
                <div className={styles.twoColumnGrid}>
                  <div>
                    <label htmlFor="role" className={styles.label}>
                      Role
                    </label>
                    <select
                      id="role"
                      name="role"
                      value={formData.role}
                      onChange={handleChange}
                      className={styles.select}
                    >
                      <option value="Admin">Admin</option>
                      <option value="Supervisor">Supervisor</option>
                      <option value="Client">Client</option>
                    </select>
                  </div>
                  <div>
                    <label htmlFor="status" className={styles.label}>
                      Status
                    </label>
                    <select
                      id="status"
                      name="status"
                      value={formData.status}
                      onChange={handleChange}
                      className={styles.select}
                    >
                      <option value="Active">Active</option>
                      <option value="Inactive">Inactive</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
            <div className={styles.card}>
              <h2 className={styles.cardTitle}>Address Information</h2>
              <div className={styles.cardContent}>
                <div>
                  <label htmlFor="country" className={styles.label}>
                    Country
                  </label>
                  <select
                    id="country"
                    name="country"
                    value={formData.country}
                    onChange={handleChange}
                    className={styles.select}
                  >
                    <option value="">Select a country</option>
                    <option value="US">United States</option>
                    <option value="CA">Canada</option>
                    <option value="UK">United Kingdom</option>
                  </select>
                </div>
                <div>
                  <label htmlFor="address" className={styles.label}>
                    Address
                  </label>
                  <input
                    type="text"
                    id="address"
                    name="address"
                    value={formData.address}
                    onChange={handleChange}
                    className={styles.input}
                  />
                </div>
                <div className={styles.twoColumnGrid}>
                  <div>
                    <label htmlFor="city" className={styles.label}>
                      City
                    </label>
                    <input
                      type="text"
                      id="city"
                      name="city"
                      value={formData.city}
                      onChange={handleChange}
                      className={styles.input}
                    />
                  </div>
                  <div>
                    <label htmlFor="postalCode" className={styles.label}>
                      Postal Code
                    </label>
                    <input
                      type="text"
                      id="postalCode"
                      name="postalCode"
                      value={formData.postalCode}
                      onChange={handleChange}
                      className={styles.input}
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className={styles.footer}>
          <button
            type="button"
            onClick={() => console.log("Back button clicked")}
            className={`${styles.button} ${styles.backButton}`}
          >
            Back
          </button>
          <button type="submit" className={styles.button}>
            Save
          </button>
        </div>
      </form>
      {error && <div className={styles.error}>{error}</div>}
      {success && <div className={styles.success}>{success}</div>}
    </div>
  );
}
