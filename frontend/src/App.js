import { useState } from "react";
import MyForm from "./components/MyForm";
import Header from "./components/Header";
import Title from "./components/Title";
import Routine from "./components/Routine";

function App() {
	const [routine, setRoutine] = useState(null);
	const [loading, setLoading] = useState(false);

	//fetch routine from api
	const fetchRoutine = async (courses) => {
		setLoading(true); //setting loading to true when we are fetching the data
		// const response = await fetch("https://cr2-api.herokuapp.com/", {
		const response = await fetch("https://cr2-backend.herokuapp.com/", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				courses: courses.courses, //this is the courses obj we got from MyForm comp as a parameter
			}),
		});

		const data = await response.json(); //getting the json data from response obj

		setLoading(false); //done loading

		return data; //return the json data
	};

	const showRoutine = (data) => {
		setRoutine([data]); //set routine with the newly fetched data
	};

	return (
		<div>
			<Header />
			<Title />
			<MyForm
				onClick={fetchRoutine}
				showRoutine={showRoutine}
				loading={loading}
				setLoading={setLoading}
			/>
			<Routine routine={routine} />
		</div>
	);
}

export default App;
