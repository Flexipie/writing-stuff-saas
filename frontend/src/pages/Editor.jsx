import React, { useState } from 'react';
import { Button } from '../components/ui/button';
import { useToast } from '../utils/use-toast';

function Editor() {
  const [content, setContent] = useState('');
  const [title, setTitle] = useState('Untitled Document');
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();

  const handleTitleChange = (e) => {
    setTitle(e.target.value);
  };

  const handleContentChange = (e) => {
    setContent(e.target.value);
  };

  const handleSave = () => {
    setLoading(true);
    
    // Simulate saving to backend
    setTimeout(() => {
      toast({
        title: 'Document Saved',
        description: `${title} has been saved successfully.`,
      });
      setLoading(false);
    }, 1000);
  };

  const handleImproveText = () => {
    if (!content.trim()) {
      toast({
        title: 'No Content',
        description: 'Please add some text to improve.',
        variant: 'destructive',
      });
      return;
    }
    
    setLoading(true);
    
    // Simulate API call to improve text
    setTimeout(() => {
      // Simple example transformation (in reality, this would come from the AI service)
      const improvedText = content
        .replace(/(?:^|\s)i(?:\s|$)/g, ' I ')
        .replace(/\s+/g, ' ')
        .trim();
      
      setContent(improvedText);
      
      toast({
        title: 'Text Improved',
        description: 'Your text has been enhanced using AI.',
      });
      
      setLoading(false);
    }, 1500);
  };

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <input
          type="text"
          value={title}
          onChange={handleTitleChange}
          className="text-2xl font-bold bg-transparent border-b border-gray-300 focus:border-primary focus:outline-none"
        />
        <div className="space-x-2">
          <Button onClick={handleImproveText} variant="outline" disabled={loading}>
            {loading ? 'Processing...' : 'Improve with AI'}
          </Button>
          <Button onClick={handleSave} disabled={loading}>
            {loading ? 'Saving...' : 'Save'}
          </Button>
        </div>
      </div>
      
      <div className="border border-gray-300 rounded-md">
        <textarea
          value={content}
          onChange={handleContentChange}
          className="w-full h-[70vh] p-4 resize-none focus:outline-none rounded-md"
          placeholder="Start writing here..."
        />
      </div>
      
      <div className="text-gray-500 text-sm">
        <p>This is a basic text editor. In the full implementation, a rich text editor like Tiptap or Slate will be integrated here.</p>
      </div>
    </div>
  );
}

export default Editor;
