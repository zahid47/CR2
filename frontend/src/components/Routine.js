import { Container, Table, Button } from "react-bootstrap";
import * as htmlToImage from 'html-to-image';

function Routine({ routine }) {
	
	//this function is really bad, please don't look inside! im too lazy to optimize this, maybe one day!
	//TODO: optimize this!!!
	const arr = [0,1,2,3,4,5]
	// const days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
	const createTable = () => (
		<Container>
			<div id="routine-table">
				<Table bordered responsive>
						<tr>
							<th></th>
							<th>08:30-10:00</th>
							<th>10:00-11:30</th>
							<th>11.30-01:00</th>
							<th>01:00-02:30</th>
							<th>02:30-04:00</th>
							<th>04:00-05:30</th>
						</tr>

						<tr>
							<td><b>Saturday</b></td>
							{arr.map((index) => (<>{routine.map((r) => (<td>{r.Saturday[index].map((c) => (<>{`${c.course_code}, ${c.teacher_initials}`}<br></br></>))}</td>))}</>))}
						</tr>

						<tr>
							<td><b>Sunday</b></td>
							{arr.map((index) => (<>{routine.map((r) => (<td>{r.Sunday[index].map((c) => (<>{`${c.course_code}, ${c.teacher_initials}`}<br></br></>))}</td>))}</>))}
						</tr>

						<tr>
							<td><b>Monday</b></td>
							{arr.map((index) => (<>{routine.map((r) => (<td>{r.Monday[index].map((c) => (<>{`${c.course_code}, ${c.teacher_initials}`}<br></br></>))}</td>))}</>))}
						</tr>

						<tr>
							<td><b>Tuesday</b></td>
							{arr.map((index) => (<>{routine.map((r) => (<td>{r.Tuesday[index].map((c) => (<>{`${c.course_code}, ${c.teacher_initials}`}<br></br></>))}</td>))}</>))}
						</tr>

						<tr>
							<td><b>Wednesday</b></td>
							{arr.map((index) => (<>{routine.map((r) => (<td>{r.Wednesday[index].map((c) => (<>{`${c.course_code}, ${c.teacher_initials}`}<br></br></>))}</td>))}</>))}
						</tr>

						<tr>
							<td><b>Thursday</b></td>
							{arr.map((index) => (<>{routine.map((r) => (<td>{r.Thursday[index].map((c) => (<>{`${c.course_code}, ${c.teacher_initials}`}<br></br></>))}</td>))}</>))}
						</tr>
					</Table>
					<p className="text-muted">Generated by https://cr2.netlify.app</p>
					<p className="text-muted">Disclaimer: This is a testing version, please double check the routine before following it. We will not be responsible for any issue this may cause. Please report any bugs using the Contact menu.</p>
			</div>
		</Container>
	);

	//check if routine obj is empty or not, returns bool
	const isEmpty = (routine) => {
		if (routine === null) {
			return true;
		} else {
			return false;
		}
	};

	const downloadRoutine = () => {

		htmlToImage.toJpeg(document.getElementById('routine-table'), { quality: 0.95, backgroundColor: "white" })
		.then(function (dataUrl) {
			var link = document.createElement('a');
			link.download = 'routine.jpeg';
			link.href = dataUrl;
			link.click();
		});

	}

	return (
		<div>
			{/* if empty show nothing otherwise show routine */}
			{isEmpty(routine) ? <></> : <>{createTable()}
				<div className="text-center btn-padding sec-btn-padding">
					<Button variant="outline-secondary" onClick={downloadRoutine}>Download</Button>
					<p className="text-muted">If you are on mobile, please use desktop mode to download or just take a screenshot</p>
				</div>
			</>}
		</div>
	);
}

export default Routine;
