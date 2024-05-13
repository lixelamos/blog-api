
# Blog Platform API

This is a simple RESTful API for a blogging platform built using FastAPI and MongoDB.

## Installation

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Start the server with `uvicorn main:app --reload`.
4. Ensure that you have mongodb installed locally,documentation is at https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/

## Usage

- Visit `/docs` endpoint to view API documentation.
- Create, read, update, and delete blog posts.
- Comment on posts.
- Like/dislike posts.
## Authentication
Authentication is not required to access the API. All endpoints are publicly accessible.

## Error Handling
The API returns appropriate HTTP status codes along with descriptive error messages in case of errors. Common error codes include:

404 Not Found: Resource not found.
400 Bad Request: Invalid request data or parameters.
500 Internal Server Error: Unexpected server error.

  ## Endpoints
 Postman was used to test this end points
 -Creating new post
 Method: POST
Request Body: JSON object representing the post.
Response: JSON object with a message indicating the success or failure of the operation along with the ID of the newly created post.
curl -X POST "http://localhost:8000/posts/" -H "Content-Type: application/json" -d '{"title": "Test Post", "content": "This is a test post content", "author": "Test User"}'
![image](https://github.com/lixelamos/blog-api/assets/48270069/0b98221b-acb2-4599-902a-468b03775c98)
Get all post
Method: GET
Response: List of JSON objects, each representing a post.
curl -X GET "http://localhost:8000/posts/"
![image](https://github.com/lixelamos/blog-api/assets/48270069/43e295e3-b52b-4b0a-a0bd-5e8b83b2c62b)
Get post by specific ID
Method: GET
Response: JSON object representing the post with the specified ID.
curl -X GET "http://localhost:8000/posts/{post_id}"
![image](https://github.com/lixelamos/blog-api/assets/48270069/94bec683-cdfc-4d96-80df-e7e09cf86cec)
Update post
Method: PUT
Request Body: JSON object representing the updated post.
Response: JSON object with a message indicating the success or failure of the operation
curl -X PUT "http://localhost:8000/posts/{post_id}" -H "Content-Type: application/json" -d '{"title": "Updated Post Title", "content": "Updated post content"}'
![image](https://github.com/lixelamos/blog-api/assets/48270069/889c239f-30eb-475e-a8d4-fd5e71280916)
Delete a post
Method: DELETE
Response: JSON object with a message indicating the success or failure of the operation.
curl -X DELETE "http://localhost:8000/posts/{post_id}"
![image](https://github.com/lixelamos/blog-api/assets/48270069/21057a6e-38f6-4b55-8770-aa0b621572eb)
Creating new comments on a post
Method: POST
Request Body: JSON object representing the comment.
Response: JSON object with a message indicating the success or failure of the operation
curl -X POST "http://localhost:8000/posts/{post_id}/comments/" -H "Content-Type: application/json" -d '{"content": "This is a test comment", "author": "Test Commenter"}'
![image](https://github.com/lixelamos/blog-api/assets/48270069/bc29c1d7-92d1-41be-bfde-7bb1780e6bc4)
Like a post
Method: POST
Response: JSON object with a message indicating the success or failure of the operation.
curl -X POST "http://localhost:8000/posts/{post_id}/like/"
![image](https://github.com/lixelamos/blog-api/assets/48270069/1f2562dd-7b13-4759-ae61-84cd01e09203)
Dislike post
Method: POST
Response: JSON object with a message indicating the success or failure of the operation
curl -X POST "http://localhost:8000/posts/{post_id}/dislike/"
![image](https://github.com/lixelamos/blog-api/assets/48270069/6c36a856-df78-4c21-9c06-44ea052ed781)

## Additional Notes
The API does not support user authentication or authorization. All actions are performed anonymously.
Posts and comments are stored in a MongoDB database. Ensure that the database connection is configured correctly before using the API.
When updating a post, both the timestamp and last_updated fields are automatically updated to the current date and time.
The API follows RESTful principles for URL structure and HTTP methods.
Use appropriate HTTP status codes and error messages to handle client requests effectively.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
