const instance = axios.create({
    baseURL: 'http://localhost:5000/api/',
    timeout: 1000,
    headers: {'X-Custom-Header': 'foobar'}
});
// 修改title为请求的数据
instance.get('/title')
.then(function (response) {
    document.title = response.data;
})
.catch(function (error) {
    console.log(error);
});