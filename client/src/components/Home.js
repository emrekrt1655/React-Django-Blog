import React from 'react'
import {Link} from 'react-router-dom'

const Home = () => {
    return (
        <div className="container">
        <div className="jumbotron mt-5">
            <h1 className="display-4">Welcome to React Blog</h1>
            <p className="lead">We make all different blog articles together..</p>
            <hr className="my-4"/>
            <p>Please click, to see the our brilliant blog articles</p>
            <Link className="btn btn-primary btn-lg" to="/blog" role="button">See More</Link>
        </div>
        </div>
    );
};

export default Home;