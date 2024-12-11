import Snowfall from 'react-snowfall';

const Homepage = () => {
    return (
        <div style={{backgroundColor:'red', height: '300px'}}>
        <Snowfall
        color="white" // Customize snowflake color
        snowflakeCount={150} // Number of snowflakes
        style={{
          position: 'fixed',
          width: '100vw',
          height: '100vh',
        }}
      />
      <h2 className='ml-auto p-0.5' >Hello World!</h2>
      <div
        style={{
          color: 'white',
          textAlign: 'center',
          paddingTop: '40vh',
          fontSize: '2rem',
        }}/>

        </div>
    )
}
export default Homepage;
