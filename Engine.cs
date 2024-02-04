namespace DSTV3.Management.TextPlainDetector.Engine
{
    public static class Engine
    {
        public static bool Scan(string text)
        {
            try
            {
                int count = 0;

                int[] validChars = new int[] { 10, 13, 1570, 1576, 1662, 40, 41, 8226, 1578, 1579, 1580, 1670, 1581, 1582, 1583,
                1584, 1585, 1586, 1688, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1601, 1602, 1705, 1711, 1604, 1605, 1606, 1608,
                1607, 1740, 1575, 8204, 1548, 1571, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1600, 65010, 46, 126, 33, 64,
                35, 36, 37, 94, 38, 42 };

                foreach (char c in text)
                {
                    if (!(32 <= (int)c && (int)c <= 126) && !validChars.Contains((int)c))
                    {
                        count += 1;
                    }
                    if (count >= 3)
                    {
                        return false;
                    }
                }
                return true;
            }
            catch (Exception ex)
            {
                // Add log
                return false;
            }
        }
    }
}