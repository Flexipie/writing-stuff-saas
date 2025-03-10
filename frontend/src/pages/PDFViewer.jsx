import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import { Button } from '../components/ui/button';
import { useToast } from '../utils/use-toast';

function PDFViewer() {
  const { id } = useParams();
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [summarizing, setSummarizing] = useState(false);
  const [summary, setSummary] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const { toast } = useToast();

  // Placeholder data - this would come from your API in the real implementation
  const documentData = {
    id,
    title: 'Sample Research Paper.pdf',
    // In a real implementation, this would be a URL to the actual PDF file
    pdfUrl: 'https://example.com/sample.pdf',
  };

  const handleSearch = (e) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;
    
    setLoading(true);
    
    // Simulate API call for semantic search
    setTimeout(() => {
      setSearchResults([
        { text: 'This is the first match containing your search terms.', page: 1, score: 0.95 },
        { text: 'Here is another section that relates to your query.', page: 3, score: 0.82 },
        { text: 'This paragraph also mentions the concepts you searched for.', page: 7, score: 0.78 },
      ]);
      
      setLoading(false);
    }, 1000);
  };

  const handleSummarize = () => {
    setSummarizing(true);
    
    // Simulate API call for document summarization
    setTimeout(() => {
      setSummary(`This is an AI-generated summary of the document "${documentData.title}".
      
The document discusses key findings in the field of artificial intelligence, particularly focusing on natural language processing and machine learning applications. The main arguments include:

1. The evolution of transformer models and their impact on language understanding
2. Ethical considerations in AI deployment
3. Future directions for research, including multimodal learning
4. Practical applications in various industries

The authors conclude that while significant progress has been made, several challenges remain to be addressed before achieving more general artificial intelligence capabilities.`);
      
      toast({
        title: 'Summary Generated',
        description: 'Document has been successfully summarized.',
      });
      
      setSummarizing(false);
    }, 2000);
  };

  return (
    <div className="flex flex-col h-[calc(100vh-12rem)]">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">{documentData.title}</h1>
        <div className="space-x-2">
          <Button 
            onClick={handleSummarize} 
            disabled={summarizing}
            variant="outline"
          >
            {summarizing ? 'Summarizing...' : 'Summarize'}
          </Button>
        </div>
      </div>
      
      <div className="flex h-full gap-4">
        {/* Main content area - PDF viewer */}
        <div className="flex-1 border border-gray-300 rounded-md p-4 bg-gray-100 overflow-auto">
          <div className="bg-white p-8 min-h-full shadow-sm rounded">
            <p className="text-center text-gray-500">
              PDF Viewer Placeholder
              <br />
              <span className="text-sm">
                (In production, this would use react-pdf to render the actual PDF)
              </span>
            </p>
            
            <div className="mt-8 p-4 border border-dashed border-gray-300 rounded">
              <p className="mb-4 text-gray-700">Sample PDF Content:</p>
              <p className="mb-2">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed id magna eget purus pulvinar vehicula.</p>
              <p className="mb-2">Praesent euismod nisi vel justo feugiat, vel ultrices nulla tempor. Nulla facilisi.</p>
              <p className="mb-2">Nullam fringilla velit vel est aliquam, id tincidunt dolor rhoncus. Vivamus auctor mauris nec.</p>
            </div>
          </div>
        </div>
        
        {/* Sidebar for search and summary */}
        <div className="w-80 border border-gray-300 rounded-md flex flex-col">
          {/* Search section */}
          <div className="p-4 border-b border-gray-300">
            <h2 className="font-medium mb-2">Search in Document</h2>
            <form onSubmit={handleSearch} className="flex">
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Enter search query..."
                className="flex-1 px-3 py-1 border border-gray-300 rounded-l-md focus:outline-none focus:ring-1 focus:ring-primary"
              />
              <Button type="submit" className="rounded-l-none" disabled={loading}>
                {loading ? '...' : 'Search'}
              </Button>
            </form>
            
            {searchResults.length > 0 && (
              <div className="mt-4 space-y-3 max-h-40 overflow-y-auto">
                {searchResults.map((result, index) => (
                  <div key={index} className="p-2 bg-gray-50 rounded text-sm">
                    <p>{result.text}</p>
                    <p className="text-xs text-gray-500 mt-1">
                      Page {result.page} • Relevance: {result.score.toFixed(2)}
                    </p>
                  </div>
                ))}
              </div>
            )}
          </div>
          
          {/* Summary section */}
          <div className="p-4 flex-1 overflow-auto">
            <h2 className="font-medium mb-2">Summary</h2>
            {summary ? (
              <div className="text-sm whitespace-pre-line">{summary}</div>
            ) : (
              <p className="text-gray-500 text-sm">
                Click the "Summarize" button to generate an AI summary of this document.
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default PDFViewer;
