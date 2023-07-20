const blogList = document.getElementById('blog-list');

const blogPost = [
    {title: 'First Blog Post', content: 'This is the first content'},
    {title: 'Second Blog Post', content: 'This is the second content '},
    {title: 'Third Blog Post', content: 'This is the third content'},
];

blogPost.forEach((post) => {
    const blogPost = document.createElement('div');
    blogPost.classList.add('blog-post');

    const title = document.createElement('h2');
    title.textContent = post.title

    const content = document.createElement('p');
    content.textContent = post.content;

    blogPost.appendChild(title);
    blogPost.appendChild(content);

    blogList.appendChild(blogPost)
})