let allBooks = [
    {
        title: 'war and peace',
        author: 'Leo tolstoy',
        image: src = 'https://russianlife.com/sites/default/cache/file/5E6BCAB5-5056-A853-0E329448D3A3CAA9_fullpage.jpg',
        alreadyRead: false
    },
    {
        title: 'in search of the miraculous',
        author: 'P.D ouspensky',
        image: src = 'https://d1w7fb2mkkr3kw.cloudfront.net/assets/images/book/lrg/9781/9469/9781946963369.jpg',
        alreadyRead: true
    }
]

const table = document.createElement('table');
table.style.border = 'solid 3px black';
table.style.padding = '15px';
table.setAttribute('id', 'table');
let creatArow = (currentBook) => {
    const tr = document.createElement('tr');
    const th = document.createElement('th');
    document.body.appendChild(table)
    tr.setAttribute('id', 'row');
    
    document.getElementById('table').appendChild(tr);
    let text1 = document.createTextNode(currentBook.title + ' by ' + currentBook.author);
    th.appendChild(text1);
    tr.appendChild(th);
    table.appendChild(row);

}
allBooks.forEach(creatArow) 









