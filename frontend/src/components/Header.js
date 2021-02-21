import { Navbar, Nav, Container } from "react-bootstrap";

function Header() {
	return (
		<Container>
			<Navbar className="white" expand="sm">
				<Navbar.Brand href="index.html">
					<img src="logo.svg"></img>
				</Navbar.Brand>
				<Navbar.Toggle aria-controls="basic-navbar-nav" />
				<Navbar.Collapse id="basic-navbar-nav">
					<Nav className="ml-auto">
						{/* <Nav.Link href="#" target="_blank">
							Help
						</Nav.Link> */}
						<Nav.Link href="https://github.com/zahid47/CR2" target="_blank">
							GitHub
						</Nav.Link>
						<Nav.Link
							href="mailto:epiczahid@gmail.com"
							target="_blank"
						>
							Contact
						</Nav.Link>
					</Nav>
				</Navbar.Collapse>
			</Navbar>
		</Container>
	);
}

export default Header;
