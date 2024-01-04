import React from 'react';
import './App.css';
import MediaDisplay from './MediaDisplay';

function App() {
  const imageUrl = 'https://s3-upload-download-test2.s3.us-west-2.amazonaws.com/image%20%281%29.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7MLx2NqYR2OHreOreMpNscpBmEeChcyanH2jj6sZxJQIgAxCWSDDc7qytPWXq0gYtoqe8%2Fetea2w%2Foc2XFblnbjUq5AIIexAAGgw4Njg2ODYzNjQxOTciDMMgb7zCPtEsA9oytirBAmeU%2FFOidIuTFTaiYL2h9q4jsopntbM4d80a0UeSpEdOCz9TmeQ35I%2BdwPeTntttcaeyu%2Bln%2BII%2Bi62BwIPD6onFPsDw%2BrdDn1QAmo2mBr%2FWbaUr7KAhMfMz7np61wnAWOM35CS%2BQnKdskLCqOBlY1%2BsDxXsEpI7tPJdZThA6R6j4%2FTSMcO0Cl8GwbeAmLhDufCPYieWwQyY3Hi04qZtcy34Zd0TlxycPqsGllCxhZ3wa944dZpKv3udFbbcpSlutG50V0anp6eWO3IbV1h7Zn2hEk96IiUwRxkq0TmdvqazDoWgkvkX1D6PFMQe4uYt4FapEIssOmYGi%2F8wzqNoJWaWxsJRv%2BuXMaF9SqDMbxJiJGTAobET7AOjBJEdp9r0JAQDVPveO%2Fb54Ve4nuUNH2h2rzhefqpPC7LK%2BV6VaZ3%2BfDCo2NusBjqzAt9reSqkB5iUv2BKN%2FQVdOCnS5tqCFaVy0UjOlf0bb0pufnG0FEa2cyQwIimFoBrhpo6cXwBmP3F%2B7%2BQih1kQcyP91g5wq%2FoDxfCF3AbY9D%2Bd9bYcTauZWN9KSw%2BFfTvzPf9ptg%2FY1GlV0W2hDsJorynHWEpnfGJCpZmgZEhfH9GbKZIgGMIZtLGbQX5jMAHY68SpVkFQA%2Bpcjo0D7M%2BBxv3lfA8k%2FY9yJT%2FN17Qfuv7K7CuDb5r2TwuRiTGtFh6b%2FbZOqeV8ycEIlfBiDWNuN9Men4bbqRDpqVqyG8zaucTY8Y900egG3Eo6yycDl5pHRF4iz%2FJ6xeM%2FIT4%2FQIdnXvp1crkrIKrSFPSMjXQlLaf3zy5b8UHxApUy7k1EnL1U%2Bv%2B8d8cOt5hZO1YK9rNmGrmGjM%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240104T180418Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=ASIA4UQN57YSQEAHRU6D%2F20240104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=0379d99775416bd240248d32cd21968b9a6ed8f329c6de64451ecded0cd38c54';
  const textFileUrl = 'https://s3-upload-download-test2.s3.us-west-2.amazonaws.com/text-gen.txt?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7MLx2NqYR2OHreOreMpNscpBmEeChcyanH2jj6sZxJQIgAxCWSDDc7qytPWXq0gYtoqe8%2Fetea2w%2Foc2XFblnbjUq5AIIexAAGgw4Njg2ODYzNjQxOTciDMMgb7zCPtEsA9oytirBAmeU%2FFOidIuTFTaiYL2h9q4jsopntbM4d80a0UeSpEdOCz9TmeQ35I%2BdwPeTntttcaeyu%2Bln%2BII%2Bi62BwIPD6onFPsDw%2BrdDn1QAmo2mBr%2FWbaUr7KAhMfMz7np61wnAWOM35CS%2BQnKdskLCqOBlY1%2BsDxXsEpI7tPJdZThA6R6j4%2FTSMcO0Cl8GwbeAmLhDufCPYieWwQyY3Hi04qZtcy34Zd0TlxycPqsGllCxhZ3wa944dZpKv3udFbbcpSlutG50V0anp6eWO3IbV1h7Zn2hEk96IiUwRxkq0TmdvqazDoWgkvkX1D6PFMQe4uYt4FapEIssOmYGi%2F8wzqNoJWaWxsJRv%2BuXMaF9SqDMbxJiJGTAobET7AOjBJEdp9r0JAQDVPveO%2Fb54Ve4nuUNH2h2rzhefqpPC7LK%2BV6VaZ3%2BfDCo2NusBjqzAt9reSqkB5iUv2BKN%2FQVdOCnS5tqCFaVy0UjOlf0bb0pufnG0FEa2cyQwIimFoBrhpo6cXwBmP3F%2B7%2BQih1kQcyP91g5wq%2FoDxfCF3AbY9D%2Bd9bYcTauZWN9KSw%2BFfTvzPf9ptg%2FY1GlV0W2hDsJorynHWEpnfGJCpZmgZEhfH9GbKZIgGMIZtLGbQX5jMAHY68SpVkFQA%2Bpcjo0D7M%2BBxv3lfA8k%2FY9yJT%2FN17Qfuv7K7CuDb5r2TwuRiTGtFh6b%2FbZOqeV8ycEIlfBiDWNuN9Men4bbqRDpqVqyG8zaucTY8Y900egG3Eo6yycDl5pHRF4iz%2FJ6xeM%2FIT4%2FQIdnXvp1crkrIKrSFPSMjXQlLaf3zy5b8UHxApUy7k1EnL1U%2Bv%2B8d8cOt5hZO1YK9rNmGrmGjM%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240104T180454Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=ASIA4UQN57YSQEAHRU6D%2F20240104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=ab013aa92e0e3943744f88a7ce19c2aebf99e9772edb16f719fc32f8f138546b';
  const videoUrl = 'https://s3-upload-download-test2.s3.us-west-2.amazonaws.com/000006.mp4?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7MLx2NqYR2OHreOreMpNscpBmEeChcyanH2jj6sZxJQIgAxCWSDDc7qytPWXq0gYtoqe8%2Fetea2w%2Foc2XFblnbjUq5AIIexAAGgw4Njg2ODYzNjQxOTciDMMgb7zCPtEsA9oytirBAmeU%2FFOidIuTFTaiYL2h9q4jsopntbM4d80a0UeSpEdOCz9TmeQ35I%2BdwPeTntttcaeyu%2Bln%2BII%2Bi62BwIPD6onFPsDw%2BrdDn1QAmo2mBr%2FWbaUr7KAhMfMz7np61wnAWOM35CS%2BQnKdskLCqOBlY1%2BsDxXsEpI7tPJdZThA6R6j4%2FTSMcO0Cl8GwbeAmLhDufCPYieWwQyY3Hi04qZtcy34Zd0TlxycPqsGllCxhZ3wa944dZpKv3udFbbcpSlutG50V0anp6eWO3IbV1h7Zn2hEk96IiUwRxkq0TmdvqazDoWgkvkX1D6PFMQe4uYt4FapEIssOmYGi%2F8wzqNoJWaWxsJRv%2BuXMaF9SqDMbxJiJGTAobET7AOjBJEdp9r0JAQDVPveO%2Fb54Ve4nuUNH2h2rzhefqpPC7LK%2BV6VaZ3%2BfDCo2NusBjqzAt9reSqkB5iUv2BKN%2FQVdOCnS5tqCFaVy0UjOlf0bb0pufnG0FEa2cyQwIimFoBrhpo6cXwBmP3F%2B7%2BQih1kQcyP91g5wq%2FoDxfCF3AbY9D%2Bd9bYcTauZWN9KSw%2BFfTvzPf9ptg%2FY1GlV0W2hDsJorynHWEpnfGJCpZmgZEhfH9GbKZIgGMIZtLGbQX5jMAHY68SpVkFQA%2Bpcjo0D7M%2BBxv3lfA8k%2FY9yJT%2FN17Qfuv7K7CuDb5r2TwuRiTGtFh6b%2FbZOqeV8ycEIlfBiDWNuN9Men4bbqRDpqVqyG8zaucTY8Y900egG3Eo6yycDl5pHRF4iz%2FJ6xeM%2FIT4%2FQIdnXvp1crkrIKrSFPSMjXQlLaf3zy5b8UHxApUy7k1EnL1U%2Bv%2B8d8cOt5hZO1YK9rNmGrmGjM%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240104T180523Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=ASIA4UQN57YSQEAHRU6D%2F20240104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=25f8d0f08db274161702212a0b3baf88dc95ad7ce2c9e26e13617404dc5aabb1';
  const audioUrl = '';

  return (
    <div className="App">
      <MediaDisplay 
        imageUrl={imageUrl} 
        textFileUrl={textFileUrl} 
        videoUrl={videoUrl} 
        audioUrl={audioUrl} 
      />
    </div>
  );
}

export default App;
