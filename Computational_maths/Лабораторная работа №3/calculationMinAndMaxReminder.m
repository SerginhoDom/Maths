function [minR, maxR] = calculationMinAndMaxReminder(func, computedX, nodes)

    syms f(x) 
    f(x) = func;
    D2f = diff(f(x), length(nodes) + 1);

    reminders = [];

    for i = 1:length(nodes)
        reminder = vpa(subs(D2f, x, nodes(i)))/factorial(length(nodes));
        reminder = abs(reminder*calculateWForReminder(computedX, nodes));
        reminders(end + 1) = reminder;
    end

    minR = min(reminders);
    maxR = max(reminders);
end