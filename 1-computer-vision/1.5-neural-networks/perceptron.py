import pandas as pd


def logical_and(test_inputs, correct_outputs):
    # TODO: Set weight1, weight2, and bias
    weight1 = 1.0
    weight2 = 1.0
    bias = -2.0
    return generate_output(weight1, weight2, bias, test_inputs, correct_outputs)


def logical_or(test_inputs, correct_outputs):
    # TODO: Set weight1, weight2, and bias
    weight1 = 1.0
    weight2 = 1.0
    bias = -1.0
    return generate_output(weight1, weight2, bias, test_inputs, correct_outputs)


def logical_not(test_inputs, correct_outputs):
    # TODO: Set weight1, weight2, and bias
    weight1 = 0.0
    weight2 = -2.0
    bias = 1.0
    return generate_output(weight1, weight2, bias, test_inputs, correct_outputs)


def generate_output(weight1, weight2, bias, test_inputs, correct_outputs):
    # Generate and check output
    outputs = []
    for test_input, correct_output in zip(test_inputs, correct_outputs):
        linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
        output = int(linear_combination >= 0)
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])
    return outputs


def main():
    # Inputs and outputs
    operation = "not"
    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    if operation == "and":
        correct_outputs = [False, False, False, True]
        outputs = logical_and(test_inputs, correct_outputs)
    elif operation == "or":
        correct_outputs = [False, True, True, True]
        outputs = logical_or(test_inputs, correct_outputs)
    elif operation == "not":
        correct_outputs = [True, False, True, False]
        outputs = logical_not(test_inputs, correct_outputs)
    else:
        print("Unknown operation: {}".format(operation))
        return

    # Print output
    num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
    output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output',
                                                  '  Is Correct'])
    if not num_wrong:
        print('Nice!  You got it all correct.\n')
    else:
        print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
    print(output_frame.to_string(index=False))


if __name__ == '__main__':
    main()