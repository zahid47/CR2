function Routine({ routine }) {
	//this function is really bad, please don't look inside! im too lazy to optimize this, maybe one day!
	//TODO: optimize this!!!
	const createTable = () => (
		<div className="table-responsive">
			<table className="table table-bordered w-50 mx-auto w-auto caption">
				<caption>Generated by https://cr2.netlify.app/</caption>
				<caption>
					Disclaimer: This is a testing version, please double check the routine
					before following it. We will not be responsible for any issue this may
					cause. Please report any bugs using the Contact menu.
				</caption>
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
					<td>
						<b>Saturday</b>
					</td>
					{routine.map((r) => (
						<td>
							{r.Saturday[0].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Saturday[1].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Saturday[2].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Saturday[3].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Saturday[4].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Saturday[5].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
				</tr>
				<tr>
					<td>
						<b>Sunday</b>
					</td>
					{routine.map((r) => (
						<td>
							{r.Sunday[0].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Sunday[1].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Sunday[2].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Sunday[3].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Sunday[4].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Sunday[5].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
				</tr>
				<tr>
					<td>
						<b>Monday</b>
					</td>
					{routine.map((r) => (
						<td>
							{r.Monday[0].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Monday[1].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Monday[2].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Monday[3].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Monday[4].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Monday[5].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
				</tr>
				<tr>
					<td>
						<b>Tuesday</b>
					</td>
					{routine.map((r) => (
						<td>
							{r.Tuesday[0].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Tuesday[1].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Tuesday[2].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Tuesday[3].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Tuesday[4].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Tuesday[5].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
				</tr>
				<tr>
					<td>
						<b>Wednesday</b>
					</td>
					{routine.map((r) => (
						<td>
							{r.Wednesday[0].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Wednesday[1].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Wednesday[2].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Wednesday[3].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Wednesday[4].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Wednesday[5].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
				</tr>
				<tr>
					<td>
						<b>Thursday</b>
					</td>
					{routine.map((r) => (
						<td>
							{r.Thursday[0].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Thursday[1].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Thursday[2].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Thursday[3].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Thursday[4].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
					{routine.map((r) => (
						<td>
							{r.Thursday[5].map((c) => (
								<>{c.course_code}</>
							))}
						</td>
					))}
				</tr>
			</table>
		</div>
	);

	//check if routine obj is empty or not, returns bool
	const isEmpty = (routine) => {
		if (routine === null) {
			return true;
		} else {
			return false;
		}
	};

	return (
		<div>
			{/* if empty show nothing otherwise show routine */}
			{isEmpty(routine) ? <></> : <>{createTable()}</>}
		</div>
	);
}

export default Routine;
