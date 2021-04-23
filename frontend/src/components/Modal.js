import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Power Analysis</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="todo-title">Base Conversion</Label>
              <Input
                type="text"
                id="power_analysis-base_conversion"
                name="base_conversion"
                value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="Enter Base Conversion"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">A Grade Proportion</Label>
              <Input
                type="text"
                id="power_analysis-a_grade_proportion"
                name="a_grade_proportion"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter A Grade Proportion"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">Uplift</Label>
              <Input
                type="text"
                id="power_analysis-uplift"
                name="uplift"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter uplift"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">Days Max</Label>
              <Input
                type="text"
                id="power_analysis-days_max"
                name="days_max"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter days max"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">Calls Per Day</Label>
              <Input
                type="text"
                id="power_analysis-calls_per_day"
                name="calls_per_day"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter Calls per Day"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}
