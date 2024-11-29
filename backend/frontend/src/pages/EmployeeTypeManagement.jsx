import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { toast } from 'react-toastify';
import { Button } from "../components/ui/button";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "../components/ui/table";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "../components/ui/dialog";
import { EmployeeTypeForm } from '../components/EmployeeTypeForm';

const API_BASE_URL = 'http://localhost:8000/masters/api/employeetypes/';

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default function EmployeeTypeManagement() {
  const [employeeTypes, setEmployeeTypes] = useState([]);
  const [isNewEntryModalOpen, setIsNewEntryModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [currentEmployeeType, setCurrentEmployeeType] = useState(null);

  useEffect(() => {
    loadEmployeeTypes();
  }, []);

  const loadEmployeeTypes = async () => {
    try {
      const response = await axios.get(API_BASE_URL);
      setEmployeeTypes(response.data);
    } catch (error) {
      console.error('Error fetching employee types:', error);
      toast.error('Failed to fetch employee types');
    }
  };

  const handleSubmit = async (formData) => {
    try {
      if (currentEmployeeType) {
        await axios.put(`${API_BASE_URL}${currentEmployeeType.id}/update/`, formData);
        toast.success('Employee type updated successfully');
      } else {
        await axios.post(`${API_BASE_URL}create/`, formData);
        toast.success('New employee type created successfully');
      }
      loadEmployeeTypes();
      setIsNewEntryModalOpen(false);
      setCurrentEmployeeType(null);
    } catch (error) {
      console.error('Error submitting data:', error);
      toast.error('Failed to submit data');
    }
  };

  const handleDelete = async () => {
    if (!currentEmployeeType) return;
    try {
      await axios.delete(`${API_BASE_URL}${currentEmployeeType.id}/delete/`);
      toast.success('Employee type deleted successfully');
      loadEmployeeTypes();
      setIsDeleteModalOpen(false);
      setCurrentEmployeeType(null);
    } catch (error) {
      console.error('Error deleting employee type:', error);
      toast.error('Failed to delete employee type');
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Employee Type Management</h1>
      
      <Dialog open={isNewEntryModalOpen} onOpenChange={setIsNewEntryModalOpen}>
        <DialogTrigger asChild>
          <Button>Add New Employee Type</Button>
        </DialogTrigger>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>{currentEmployeeType ? "Edit Employee Type" : "New Employee Type"}</DialogTitle>
          </DialogHeader>
          <EmployeeTypeForm
            initialData={currentEmployeeType || undefined}
            onSubmit={handleSubmit}
            isEditing={!!currentEmployeeType}
          />
        </DialogContent>
      </Dialog>

      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>ID</TableHead>
            <TableHead>Name</TableHead>
            <TableHead>Description</TableHead>
            <TableHead>Code</TableHead>
            <TableHead>Actions</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {employeeTypes.map((employeeType) => (
            <TableRow key={employeeType.id}>
              <TableCell>{employeeType.id}</TableCell>
              <TableCell>{employeeType.name}</TableCell>
              <TableCell>{employeeType.description}</TableCell>
              <TableCell>{employeeType.code}</TableCell>
              <TableCell>
                <Button
                  variant="outline"
                  onClick={() => {
                    setCurrentEmployeeType(employeeType);
                    setIsNewEntryModalOpen(true);
                  }}
                  className="mr-2"
                >
                  Edit
                </Button>
                <Button
                  variant="destructive"
                  onClick={() => {
                    setCurrentEmployeeType(employeeType);
                    setIsDeleteModalOpen(true);
                  }}
                >
                  Delete
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>

      <Dialog open={isDeleteModalOpen} onOpenChange={setIsDeleteModalOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Confirm Deletion</DialogTitle>
          </DialogHeader>
          <p>Are you sure you want to delete this employee type?</p>
          <div className="flex justify-end space-x-2">
            <Button variant="outline" onClick={() => setIsDeleteModalOpen(false)}>Cancel</Button>
            <Button variant="destructive" onClick={handleDelete}>Delete</Button>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}

