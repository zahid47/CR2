import { Container, Table } from "react-bootstrap";

function Routine({ routine }) {
  const arr = [0, 1, 2, 3, 4, 5];
  const days = [
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
  ];

  const createTable = () => (
    <Container>
      <div id="routine-table">
        <Table bordered responsive>
          <thead>
            <tr>
              <th></th>
              <th>08:30-10:00</th>
              <th>10:00-11:30</th>
              <th>11.30-01:00</th>
              <th>01:00-02:30</th>
              <th>02:30-04:00</th>
              <th>04:00-05:30</th>
            </tr>
          </thead>

          <tbody>
            {days.map((day) => (
              <tr>
                <td>
                  <b>{day}</b>
                </td>
                {arr.map((index) => (
                  <>
                    {routine.map((r) => (
                      <td>
                        {r[day][index].map((c) => (
                          <>
                            {`${c.course_code}, ${c.teacher_initials}`}
                            <br></br>
                          </>
                        ))}
                      </td>
                    ))}
                  </>
                ))}
              </tr>
            ))}
          </tbody>
        </Table>
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

  return (
    <div>
      {/* if empty show nothing otherwise show routine */}
      {!isEmpty(routine) ? createTable() : <></>}
    </div>
  );
}

export default Routine;
