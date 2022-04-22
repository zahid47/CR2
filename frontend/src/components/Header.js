import { Navbar, Nav, Container } from "react-bootstrap";

function Header() {
  return (
    <Container>
      <Navbar className="white" expand="sm">
        <Navbar.Brand href="index.html">
          <img alt="cr2 logo" src="logo.svg"></img>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto">
            <Nav.Link href="https://github.com/zahid47/CR2" target="_blank">
              source
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    </Container>
  );
}

export default Header;
