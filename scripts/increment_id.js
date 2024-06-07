const fs = require('fs');

let postData = null;

// Function to generate and update incrementing ID
function generateIncrementId() {
  const path = require('path');
  const idFilePath = path.join(process.cwd(), 'scripts/increment_id.txt');
  let id = 1;

  // Read the current ID from the file, if it exists
  if (fs.existsSync(idFilePath)) {
    const idContent = fs.readFileSync(idFilePath, 'utf8');
    id = parseInt(idContent) + 1;
  }

  // Save the new ID back to the file
  fs.writeFileSync(idFilePath, id.toString(), 'utf8');
  return id;
}

hexo.extend.filter.register('new_post_path', function(data) {
  postData = data;
  return data;
});

// Register filter for new post creation
hexo.extend.filter.register('before_exit', function() {

  if (!postData) {
    return;
  }

  // Read the newly created post file
  const postContent = fs.readFileSync(postData, 'utf8');

  // Generate new increment ID
  const newId = generateIncrementId();

  // Replace the placeholder with the actual ID
  const newContent = postContent.replace('increment_id', newId);

  // Write the updated content back to the post file
  fs.writeFileSync(postData, newContent, 'utf8');

  return postData;
});
