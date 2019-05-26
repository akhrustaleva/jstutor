# Men:   BMR = 10W + 6.25H - 5A + 5
# Women: BMR = 10W + 6.25H - 5A - 161

# W - weight (kg)
# H - height (cm)
# A - age (years)


def bmr(gender, weight, height, age ):
    if gender == 'm':
        return 10 * weight + 6.25 * height - 5 * age + 5
    return 10 * weight + 6.25 * height - 5 * age - 161


def main():
    print(str(bmr(gender='m', age=25, weight=65, height=180)) + ' ==  1655')
    print(str(bmr(gender='f', age=70, weight=48, height=162)) + ' ==  982')
    print(str(bmr(gender='f', age=24, weight=44, height=165)))


if __name__ == '__main__':
    main()
