import { useState } from "react";
import { Container, Form, Button } from "react-bootstrap";

function MyForm({ onClick, showRoutine, loading }) {
	const [courses, setCourses] = useState("");

	const onSubmit = async (e) => {
		await e.preventDefault();
		if (courses != "") {
			//making sure the courses text field is not empty
			const data = await onClick({ courses }); //onClick called the function fetchRoutine in App.js and here we are also sending courses a parameter
			await showRoutine(data); //showRoutine is a function in App.js (is just calls setRoutine which then updates the routine state and shows the routine that we got from api)
		} else {
			//course text field is empty
			alert("Please enter at-least one course.");
		}
	};

	return (
		<Container>
			<Form className="my-form" onSubmit={onSubmit}>
				<Form.Group>
					<Form.Control
						type="text"
						placeholder="Courses with Section"
						value={courses}
						onChange={(e) => {
							setCourses(e.target.value);
						}}
					/>
					<Form.Text className="text-muted">
						separate them with a comma. Like: PHY101A,MAT102B
					</Form.Text>
				</Form.Group>
				<div className="text-center btn-padding">
					{!loading && (
						<Button variant="primary" type="submit">
							Get Routine
						</Button>
					)}
					{loading && (
						<Button variant="primary" type="submit" disabled>
							Please Wait
						</Button>
					)}
				</div>
			</Form>
		</Container>
	);
}

export default MyForm;
