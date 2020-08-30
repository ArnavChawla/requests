let baseUrl = 'http://ec2-34-210-108-229.us-west-2.compute.amazonaws.com/api/v1';

if (process.env.NODE_ENV && process.env.NODE_ENV === 'development') {
  baseUrl = 'http://ec2-34-210-108-229.us-west-2.compute.amazonaws.com/api/v1';
}

const requestsUrl = `${baseUrl}/requests`;
const requestUrl = id => `${baseUrl}/requests/${id}`;
const requestCommentsUrl = id => `${baseUrl}/requests/${id}/comments`;
const clientsUrl = id => `${baseUrl}/clients/${id}`;
const staffUrl = id => `${baseUrl}/staff/${id}`;

export {
  requestsUrl,
  requestUrl,
  requestCommentsUrl,
  clientsUrl,
  staffUrl,
};
