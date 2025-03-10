import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Button } from '../components/ui/button';
import { useToast } from '../utils/use-toast';

function Dashboard() {
  const [documents, setDocuments] = useState([
    { id: 1, title: 'Research Paper.pdf', date: '2025-03-09', size: '1.2 MB' },
    { id: 2, title: 'My Essay.pdf', date: '2025-03-08', size: '0.8 MB' },
    { id: 3, title: 'Notes.pdf', date: '2025-03-07', size: '0.5 MB' },
  ]);
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (!file) return;
    
    if (!file.name.endsWith('.pdf')) {
      toast({
        title: 'Invalid File',
        description: 'Please upload a PDF file',
        variant: 'destructive',
      });
      return;
    }

    setLoading(true);
    
    // Simulate file upload
    setTimeout(() => {
      const newDoc = {
        id: documents.length + 1,
        title: file.name,
        date: new Date().toISOString().split('T')[0],
        size: `${(file.size / (1024 * 1024)).toFixed(1)} MB`,
      };
      
      setDocuments([newDoc, ...documents]);
      
      toast({
        title: 'Upload Successful',
        description: `${file.name} has been uploaded`,
      });
      
      setLoading(false);
    }, 1500);
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold">Your Documents</h1>
        <div>
          <input
            type="file"
            id="file-upload"
            accept=".pdf"
            className="hidden"
            onChange={handleFileUpload}
            disabled={loading}
          />
          <label htmlFor="file-upload">
            <Button as="span" className="cursor-pointer" disabled={loading}>
              {loading ? 'Uploading...' : 'Upload PDF'}
            </Button>
          </label>
          <Link to="/editor">
            <Button variant="outline" className="ml-2">
              New Document
            </Button>
          </Link>
        </div>
      </div>
      
      {documents.length === 0 ? (
        <div className="text-center py-12 bg-gray-50 rounded-lg">
          <p className="text-gray-500">You haven't uploaded any documents yet.</p>
          <p className="text-gray-500 mt-2">Upload a PDF to get started!</p>
        </div>
      ) : (
        <div className="overflow-x-auto">
          <table className="w-full border-collapse">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-4 py-2 text-left">Title</th>
                <th className="px-4 py-2 text-left">Date</th>
                <th className="px-4 py-2 text-left">Size</th>
                <th className="px-4 py-2 text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {documents.map((doc) => (
                <tr key={doc.id} className="hover:bg-gray-50">
                  <td className="px-4 py-3">{doc.title}</td>
                  <td className="px-4 py-3">{doc.date}</td>
                  <td className="px-4 py-3">{doc.size}</td>
                  <td className="px-4 py-3 text-right space-x-2">
                    <Link to={`/pdf/${doc.id}`}>
                      <Button variant="outline" size="sm">View</Button>
                    </Link>
                    <Button variant="outline" size="sm" className="text-red-500 hover:text-red-700">
                      Delete
                    </Button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Dashboard;
