import React from 'react'
import { useState } from 'react'
import { useDispatch } from "react-redux";
import { useNavigate } from 'react-router-dom'
import { setFile } from '../redux/files/file'

export default function UploadForm() {
  const [file, setlocalFile] = useState(null)
  const [uploading, setUploading] = useState(false)
  const[loading,setloading]=useState(false);
  const [message, setMessage] = useState('')
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const handleFileChange = (e) => {
    setMessage('')
    const f = e.target.files && e.target.files[0]
    setlocalFile(f || null)
    dispatch(setFile({ file: f || null, previewUrl: f ? URL.createObjectURL(f) : null }));
  }

  const handleUpload = async (e) => {
    e.preventDefault()
    if (!file) return setMessage('Please choose a file first')

    const formData = new FormData()
    formData.append('file', file)

    try {
      setUploading(true)
      setMessage('')
      const res = await fetch('http://127.0.0.1:8000/api/upload', {
        method: 'POST',
        body: formData,
      })
      setloading(true);

      if (!res.ok) {

        const text = await res.text()
        throw new Error(text || `Upload failed: ${res.status}`)
        setloading(false);
      }

      const data = await res.json().catch(() => null)
      console.log('Upload response data:', data)
      setloading(false);
      setMessage(data?.message || 'Upload successful')
      setlocalFile(null)
      navigate('/answerbox')
      // clear the file input value by resetting the form (see DOM below)
      e.target.reset && e.target.reset()
     
    } catch (err) {
      setMessage(err.message || 'Upload error')
    } finally {
      setUploading(false)
    }
  }

  return (
    <div className="w-screen h-screen bg-gray-300">
      <form onSubmit={handleUpload} className="max-w-md mx-auto p-6 bg-white rounded-lg shadow-md">
        <h2 className="text-2xl font-bold mb-4 text-gray-800">Upload a file</h2>

        <div className="mb-4">
          <input
            type="file"
            name="file"
            onChange={handleFileChange}
            aria-label="Choose file to upload"
            className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
          />
        </div>

        {file && (
          <div className="mb-4 p-2 bg-gray-100 rounded">
            <strong className="text-gray-700">Selected:</strong> {file.name} ({Math.round(file.size / 1024)} KB)
          </div>
        )}

        <div className="flex space-x-2 mb-4">
          <button
            type="submit"
            disabled={uploading || !file}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed"
          >
            {uploading ? 'Uploading...' : 'Upload'}
          </button>
          <button
            type="button"
            onClick={() => {
              setlocalFile(null)
              setMessage('')
              // clear native input (find input and reset)
              const inp = document.querySelector('input[type=file][name=file]')
              if (inp) inp.value = ''
            }}
            className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
          >
            Clear
          </button>
        </div>

        {message && (
          <div className="text-sm italic text-gray-600">
            {message}
          </div>
        )}
      </form>
      
    </div>
  )
}